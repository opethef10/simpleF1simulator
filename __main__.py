from Session import Session
import json#,   yaml

session=Session()
session.simulate()
json.dump(session,open("io/out.json","w"),default=vars,indent=4)
#yaml.dump(yaml.load(open("io/out.json")),open("io/out.yaml","w"),default_flow_style=False,indent=4,sort_keys=False)
for car in session.carList: print(car.driver, car.fastestLap)