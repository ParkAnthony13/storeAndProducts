from store import *

onlyDucks = Store("Only Ducks")
onlyDucks.product_line().add_product("Yellow Duck",5,"bath").add_product("Gun Duck",15,"combat").product_line()

onlyDucks.sell_product(0).product_line()

onlyDucks.add_product("Sky Duck",20,"flying").add_product("Graduate Duck",12,"school").product_line()

onlyDucks.inflation(0.05).inflation(0.05).inflation(0.05)
onlyDucks.product_line()


onlyDucks.set_clearance("flying",0.05).set_clearance("flying",0.05).set_clearance("flying",0.05)
onlyDucks.product_line()