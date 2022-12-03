import random
import time

print("""
    ขอต้อนรับสู่---------------------------------------
    -----------------------------------------------
    ///////  ///////  ///////  //  //   //  /////// 
    //       //   //  //       //  ///  //  //   //
    //       //   //  ///////  //  // / //  //   //
    //       ///////       //  //  //  ///  //   //
    ///////  //   //  ///////  //  //   //  ///////
    ------------------------------- บ่อนไฮโลถูกกฎหมาย
    -----------------------------------------------""")

print("เริ่มเล่น [s] ออก[q]")
start = input("<<< ")

if start == 's':
    print(">>> กรุณาแลกชิพ")
    chip = int(input("<<< "))
    hilow_list = []
    teng_list = []
    tod_list = []

    while True:
        print("\nลูกเต๋าถูกเขย่าแล้ว.....")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)

        dice1 = random.randint(1, 7)
        dice2 = random.randint(1, 7)
        dice3 = random.randint(1, 7)

        while True:
            print("\n>>> เลือกวิธีการเล่น สูงต่ำ[h] เต็ง[s] โต้ด[m] ยกเลิก[q]")
            play_method = input("<<< ")

            if play_method == "h":
                print("\n>>> คุณเลือกเล่นสูงต่ำ")

                print(">>> กรุณาเลือกแต้ม สูง[h] ต่ำ[l] 11[11]")
                input_hilow = input("<<< ")

                if input_hilow == "h":
                    input_hilow = "สูง"

                elif input_hilow == "l":
                    input_hilow = "ต่ำ"

                elif input_hilow == "11":
                    input_hilow = "11 ไฮโล"

                else:
                    print(">>> คุณป้อนข้อมูลไม่ถูกต้อง")
                    continue

                print(">>> วางเงิน")
                input_money = int(input("<<< "))

                hilow_list.append([input_hilow, input_money])

            elif play_method == "s":
                print("\n>>> คุณเลือกเล่นเต็ง")

                print(">>> กรุณาเลือกแต้ม 1, 2, 3, 4, 5, 6")
                input_teng = int(input("<<< "))

                if 0 < input_teng < 7:
                    pass

                else:
                    print(">>> คุณป้อนข้อมูลไม่ถูกต้อง")
                    continue

                print(">>> วางเงิน")
                input_money_teng = int(input("<<< "))

                teng_list.append([input_teng, input_money_teng])

            elif play_method == "m":
                print("\n>>> คุณเลือกเล่นโต้ด")

                print(">>> กรุณาเลือกแต้ม 1, 2, 3, 4, 5, 6")
                input_teng1 = int(input("<<< "))

                if 0 < input_teng1 < 7:
                    pass

                else:
                    print(">>> คุณป้อนข้อมูลไม่ถูกต้อง")
                    continue

                print(">>> กรุณาเลือกแต้ม 1, 2, 3, 4, 5, 6")
                input_teng2 = int(input("<<< "))

                if 0 < input_teng2 < 7:
                    pass

                else:
                    print(">>> คุณป้อนข้อมูลไม่ถูกต้อง")
                    continue

                print(">>> วางเงิน")
                input_money_teng = int(input("<<< "))

                tod_list.append([input_teng1, input_teng2, input_money_teng])

            print("\n>>> คุณต้องการเพิ่มเดิมพันอีกหรือไม่ [y]ใช่ [n]ไม่ ")
            q = input("<<< ")

            if q == 'n':
                break

            elif q == 'y':
                pass

            else:
                print(">>> คุณป้อนคำสั่งไม่ถูกต้อง\n")
                continue

        if len(hilow_list) > 0 or len(teng_list) > 0 or len(tod_list) > 0:
            print()
            print("=" * 20, "เปิด")
            print(f">>> แต้มลูกเต๋า {dice1} {dice2} {dice3}")

        sum_dice = dice1 + dice2 +dice3

        if sum_dice < 11:
            hi_low = "ต่ำ"

        elif sum_dice > 11:
            hi_low = "สูง"

        else:
            hi_low = "11 ไฮโล"

        # cale high low
        if len(hilow_list) > 0:
            print(f"แต้ม {hi_low}")
            for i in hilow_list:
                if i[0] == hi_low and i[0] == "11 ไฮโล":
                    chip += (i[1] * 5)
                    print(f">>> คุณเดิมพัน {i[0]} ได้รับเงิน {i[1] * 5}")

                elif i[0] == hi_low and i[0] != "11 ไฮโล":
                    chip += i[1]
                    print(f">>> คุณเดิมพัน {i[0]} ได้รับเงิน {i[1]}")

                if i[0] != hi_low:
                    chip -= i[1]
                    print(f">>> คุณเดิมพัน {i[0]} เสียเงิน {i[1]}")

            print(f">>> เงินของคุณเหลือ {chip}")

        # cale teng
        if len(teng_list) > 0:
            t = 0
            for teng in teng_list:
                if teng[0] == dice1:
                    t += 1
                elif teng[0] == dice2:
                    t += 1
                elif teng[0] == dice3:
                    t += 1
                else:
                    t -= 1

                if t > 0:
                    print(f">>> คุณเดิมพัน {teng[0]} ได้รับเงิน {teng[1]} * {t} = {teng[1] * t}")
                else:
                    print(f">>> คุณเดิมพัน {teng[0]} เสียเงิน {teng[1]}")

                chip += (t * teng[1])

            print(f">>> เงินของคุณเหลือ {chip}")

        # cale tod
        if len(tod_list) > 0:
            for tod in tod_list:
                if (tod[0] == dice1 or tod[0] == dice2 or tod[0] == dice3) \
                    and (tod[1] == dice1 or tod[1] == dice2 or tod[1] == dice3):
                    chip += (tod[2] * 5)

                    print(f"คุณเดิมพัน โต้ด {tod[0]} และ {tod[1]} ได้รับเงิน {tod[2] * 5}")

                else:
                    chip -= tod[2]
                    print(f"คุณเดิมพัน โต้ด {tod[0]} และ {tod[1]} เสียเงิน {tod[2]}")

            print(f">>> เงินของคุณเหลือ {chip}")
        print("=" * 20)
        print("\n>>> คุณต้องการเล่นต่อหรือไม่ เล่นต่อ[y or any] ออก[q]")
        start = input("<<< ")

        if start == "q":
            print("\nขอบคุณที่ใช้บริการ.....")
            break
        else:
            teng_list = []
            tod_list = []
            hilow_list = []

else:
    print("\nขอบคุณที่ใช้บริการ.....")
