import importlib.util,pathlib,json
p=pathlib.Path(__file__).parent
s=importlib.util.spec_from_file_location("calculator",p/"decision-calculator.py");m=importlib.util.module_from_spec(s);s.loader.exec_module(m)
d=json.loads((p/"example-assumptions.json").read_text());r=m.compare(d)
assert r["manual_total_minutes"]==120 and r["automation_total_minutes"]==110
d["runs"]=2;r=m.compare(d)
assert r["manual_total_minutes"]==12 and r["automation_total_minutes"]==60.5
for bad in [-1,True,float("nan"),None]:
 d["runs"]=bad
 try: m.compare(d)
 except (ValueError,TypeError): pass
 else: raise AssertionError("Invalid input accepted")
print("PASS: two arithmetic cases; negative, boolean, nonfinite and unknown inputs rejected")
