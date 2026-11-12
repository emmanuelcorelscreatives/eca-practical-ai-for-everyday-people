(function(root){
'use strict';
const allowed=['eventTitle','approvedDescription','dateAndTime','venue','sourceRecordId'];
const destination='Community events page — draft area';
function initial(){return {version:1,paused:false,externalActionEnabled:false,queue:[],history:[],pauseLog:[]};}
function mapped(input){return Object.fromEntries(allowed.map(k=>[k,input[k]||'']));}
function draft(input){return 'DRAFT — NOT PUBLISHED\n'+input.eventTitle+'\n'+input.dateAndTime+' — '+input.venue+'\n'+input.approvedDescription+'.\n\nMissing information: accessibility details; booking requirements; organizer contact.';}
function prepare(state,input,now){
 if(state.paused){state.history.push({at:now,status:'No new trigger accepted after pause',externalAction:'Not run'});return {accepted:false,reason:'paused'};}
 if(input.form!=='Approved event form'||input.folder!=='Training submissions'||input.status!=='Ready for drafting')return {accepted:false,reason:'outside permitted trigger'};
 const day=new Date(now).getUTCDay(),hour=new Date(now).getUTCHours();
 // This training workspace deliberately uses UTC as its local timezone.
 if(!Number.isFinite(day)||day===0||day===6||hour<9||hour>=16)return {accepted:false,reason:'outside staffed review hours (UTC training workspace)'};
 if(state.queue.some(q=>q.sourceRecordId===input.sourceRecordId))return {accepted:false,reason:'source already saved'};
 const snapshot=mapped(input),q={queueId:'CEA-'+String(state.queue.length+1).padStart(4,'0'),sourceRecordId:input.sourceRecordId,inputSnapshot:snapshot,draft:draft(snapshot),proposedDestination:destination,status:'Awaiting review',reviewerDecision:'Not decided',createdAt:now,decisionAt:null};
 state.queue.push(q);state.history.push({at:now,status:'Completed — review record saved',queueId:q.queueId,externalAction:'Not run'},{at:now,status:'Waiting — approval',queueId:q.queueId,externalAction:'Not run'});return {accepted:true,queueId:q.queueId};
}
function pause(state,owner,reason,now){if(!owner.trim()||!reason.trim())throw Error('Record owner and reason');state.paused=true;state.externalActionEnabled=false;state.pauseLog.push({owner,reason,at:now});}
function externalAction(){throw Error('External publishing is absent from this offline training app.');}
const api={allowed,destination,initial,mapped,draft,prepare,pause,externalAction};
if(typeof module!=='undefined'&&module.exports)module.exports=api;else root.AcademyWorkflow=api;
})(typeof globalThis!=='undefined'?globalThis:this);
