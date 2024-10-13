#Variables
hrs_per_wk = int(input("hrs of work: ")) 
hrly_pay = int(150)
ot_pay = hrly_pay * 0.5
   
if 0 < hrs_per_wk < 168:
    if hrs_per_wk > 40:
        ot_slry = (hrly_pay*hrs_per_wk) + ot_pay
        print("sipag mo naman, ito sweldo mo weekly:", ot_slry)
        mthly_slry = ot_slry*4
        print("pre-tax sweldo mo:", mthly_slry)
        
        
        if 10000 < mthly_slry >= 50000:
            taxed_slry = mthly_slry*0.9
            print("swildo (post-tax):", taxed_slry)
        elif 50000 < mthly_slry:
            taxed_slry = mthly_slry*0.8
            print("yaman mo lods, kaso mag ambag ka sa gobyerno:", taxed_slry)
        else:
            print("eyy wala tax")
    
    
    else:
        
        slry = (hrly_pay*hrs_per_wk)
        print("swildo ng tamad (per week):", slry)
        mthly_slry = slry*4
        print("monthly salary:", slry*4)



else:
    print("di yan edewps, please enter a valid hour time")