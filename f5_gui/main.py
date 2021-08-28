
import tkinter 
import csv
import os
import os
import threading
import time
from queue import Queue
import copy as c


table_queue = Queue()  
big_cat_queue = Queue()
last_ops_queue = Queue()
user_big_cat = "nonn"


def GUI_main() :
    root = tkinter.Tk()
    canvas = tkinter.Canvas(width = 800, height = 600)
    canvas.pack()
    #mina = tkinter.PhotoImage(file = "mina.png")
    #canvas.create_image(400, 300, image = mina)
    button = tkinter.Button(text = "확인", font = ("System", 32))
    button.place(x = 400, y = 480)

    #text = tkinter.Text(width = 40 , height = 5, font = ("System", 16))
    #text.place(x = 320, y = 30)

    root.mainloop()

class prints :
    def print_list(table) :
        for i in table :
            print(i)
    
    def print_div_6(table) :
        for i in range(len(table)) :
            if i % 6 == 0 and i != 0:
                print()
            print(table[i],end="\t")
            if prints.get_real_length_on_CMD(table[i]) < 8 :
                print("\t\t",end="")
            elif prints.get_real_length_on_CMD(table[i]) < 16 :
                print("\t",end="")

    def get_real_length_on_CMD(string) :
        count = 0
        for i in range(len(string)) :
            if string[i].encode().isdigit() :
                count += 1
            else :
                if string[i] == "]" or string[i] == "[" or string[i] == ")" or string[i] == "(" or string[i] == " " or string[i] == ","or string[i] == "." or string[i].encode().isalpha():
                    #영어 맞음
                    count += 1
                else :
                    count += 2 
        #print("GRLOC :",count)
        return count
    
    def print_div_6_on_label(table) :
        answer = ""
        for i in range(len(table)) :
            if i % 6 == 0 and i != 0:
                answer += "\n"
            #print(table[i],end="\t")
            answer += table[i]+"\t"
            if prints.get_real_length_on_CMD(table[i]) < 8 :
                #print("\t\t",end="")
                answer += "\t\t"
            elif prints.get_real_length_on_CMD(table[i]) < 16 :
                #print("\t",end="")
                answer += "\t"
        print("prints print div 6 on label :",answer)
        text["text"] = answer
        os.system("pause")
        return answer
    
    def get_div_6_on_listbox(table,listbox) :
        print(type(listbox))

        
        for i in range(len(table)) :
            if i % 6 == 0 and i != 0:
                print()
            print(table[i],end="\t")
            adds = ""
            if prints.get_real_length_on_CMD(table[i]) < 8 :
                #print("\t\t",end="")
                adds = "\t\t"
            elif prints.get_real_length_on_CMD(table[i]) < 16 :
                #print("\t",end="")
                adds = "\t"
            listbox.insert(i,str(table[i])+"\t"+adds)

        #os.system("pause")
        #for line in range(1,1001):
        #    listbox.insert(line, str(line) + "/1000")
        listbox.pack(side="right")
        return listbox



class setting :

    

    def setting_column_on_queue() :
        while True :
            try :
                table_tuple = table_queue.get()
                table_queue.put([table_tuple["품목명"],table_tuple["단위"],table_tuple["등급"],table_tuple["가격"]])
            except :
                break
    
    def setting_column_on_queue_bit_cat() :
        

        
        for i in range(int(table_queue.qsize())//thread_count) :
            try :

                table_tuple = table_queue.get()
                #print("table_tuple :",table_tuple)
                temp = str(table_tuple[0]).split("]")
                #print("temp1 :",temp)
                del temp[0]
                #print("temp2 :",temp)
                temp = str(temp[0]).split("(")[0]
                #print("temp3 :",temp)   
                big_cat_queue.put(temp)

                table_queue.put(table_tuple)

            except :
                break
    def synchronization_queue_to_table(table) :
        for i in table :
            table_queue.put(i)
        pass


    def get_table(filepath) :
            #table.csv
            table = []
            with open(filepath,'r') as f :
                reader = csv.DictReader(f)
                for row in reader :
                    table.append(row)
                    #print(row)
            return table

    def setting_column(table) :
        res = []
        for i in table :
            temp_li = [i["품목명"],i["단위"],i["등급"],i["가격"]]
            #print("setting_column tmp_li :",temp_li)
            if not i in res :
                #print(i)
                res.append(temp_li)
        return res
    def duplicate_deficiencying_name(table) :
        prints.print_list(table)
        kinds_lv1 = []
        for i in table :
            if i[0] not in kinds_lv1 :
                kinds_lv1.append(i[0])
        print("duplicate_deficiencying kinds_lv1 :",kinds_lv1)
        prints.print_list(kinds_lv1)

        kinds_lv2 = []
        for i in table :
            if i[1] not in kinds_lv2 :
                kinds_lv2.append(i[1])
        print("duplicate_deficiencying kinds_lv2 :",kinds_lv2)
        prints.print_list(kinds_lv2)
        
        
        kinds_lv3 = []
        for i in table :
            if i[2] not in kinds_lv3 :
                kinds_lv3.append(i[2])
        #print("duplicate_deficiencying kinds_lv3 :",kinds_lv3)
        #prints.print_list(kinds_lv3)
        
        kinds_res_cat_t = []
        for i in table :
            temp_list = [i[0],i[1],i[2]]
            if temp_list not in kinds_res_cat_t :
                kinds_res_cat_t.append(temp_list)
        kinds_res_cat = []
        for i in kinds_res_cat_t :
            kinds_res_cat.append([i,[]])
        print("table :")
        prints.print_list(table)
        print("kinds_res_cat :")
        prints.print_list(kinds_res_cat)
        #kinds_res_cat[0][1].append(1)
        #print(kinds_res_cat[0][1][0])
        #os.system('pause')
        res = []
        for i in kinds_lv1 :
            #print("i :",i)
            for j in kinds_lv2 :
                for k in kinds_lv3 :
                    for e in table :
                        #print("e :",e)
                        if e[0] == i and e[1] == j and e[2] == k :
                            t_title = [e[0],e[1],e[2]]
                            #print(t_title)
                            for n in kinds_res_cat :
                                #print("n[0] == t_title :",n[0] == t_title)
                                #print("n[0] :",n[0] )
                                #print("t_title :",t_title)
                                #os.system('pause')
                                if n[0] == t_title :
                                    #print("1n :",n)
                                    #print("2n[0] :",n[0])
                                    #print("3n[1] :",n[1])
                                    #print("4appending target e[3]:",e[3])
                                    n[1].append(e[3])
                                    #print("5n :",n)
                                    #print("6n[0] :",n[0])
                                    #print("7n[1] :",n[1])
        print("1kinds_res_cat; res :",kinds_res_cat)
        prints.print_list(kinds_res_cat)    
        for i in kinds_res_cat :
            temp_res = 0
            for j in i[1] :
                temp_res += int(j)
            temp_res = temp_res // len(i[1])
            i[1] = temp_res
        print("2kinds_res_cat; res :",kinds_res_cat)

        prints.print_list(kinds_res_cat)
        return kinds_res_cat  
    def integrating_list (target_list) :
        '''

        [['[사과]로얄부사', '10kg', '특(1등)'], 23828]
        [['[사과]로얄부사', '10kg', '상(2등)'], 9181]
        [['[사과]부사(사과)', '10kg', '보통(3등)'], 10800]
        '''
        print("intergrating_list target_list :")
        prints.print_list(target_list)
        res = []
        for i in target_list :
            print("intergrating_list i :",i)
            print("intergrating_list i[0][0] :",i[0][0])
            print("intergrating_list i[0][1] :",i[0][1])
            print("intergrating_list i[0][2] :",i[0][2])
            print("intergrating_list i[1] :",i[1])
            res.append([i[0][0],i[0][1],i[0][2],i[1]])
        print("intergrating_list res : ")
        prints.print_list(res)
        return res
    def sorting_grade(kinds_lv2) :
        print('sorting_grade kinds_lv2 :')
        prints.print_list(kinds_lv2)
        tres1 = []
        tres2 = []

        for i in kinds_lv2 :
            tres1.append(str(i).split("kg")[0])
        for i in range(len(tres1)) :
            if list(tres1[i])[0] == '.' :
                tres1[i] = "0"+str(tres1[i])
        
        temps1 = [[],[],[],[]]
        for i in tres1 :
            temps1[len(str(str(i).split(".")[0])) - 1].append(i)
        
        for i in range(len(temps1)) :
            for j in range(len(temps1[i])) :
                try :
                    temps1[i][j] = int(temps1[i][j])
                finally :
                    temps1[i][j] = float(temps1[i][j])

        temps1.sort(key=lambda x:x[0])
        
                
 
        print("sorting_grade tres1 :",tres1)
        print("sorting_grade temps1 :")
        prints.print_list(temps1)
        pass
        
class selects :

    def select_lv1_category(table) :
        res = []
        for i in table :
            temp_li = str(i[0]).split("]")
            temp_li = list(temp_li)
            del temp_li[0]
            temp_li = "".join(temp_li)
            if temp_li not in res :
                res.append(temp_li)
        prints.print_list(res)
        return res
    
    def select_lv2_category(table,cat_name) :
        res = []
        for i in table :
            #print("select lv2 category i:",i)
            if cat_name in i[0] :
                if i not in res :

                    print("select lv2 category appending culomn :",i)
                    res.append(i)

        #prints.print_list("select lv2 category res :",res)
        return res
    

class sectors :
    def sector1() :
        print("sector 1 enterd")
        
        text["text"] = "sector 1 enterd"
        
        table = []
        table = setting.get_table("table.csv")
        #print("len(table) bf :",len(table))

        setting.synchronization_queue_to_table(table)
        #table = setting.setting_column(table)
        #print("len(table) af :",len(table))
        #prints.print_list(table)

        
        for j in range(thread_count) :
            #print("thread {} entered ".format(j))
            thread = threading.Thread(target=setting.setting_column_on_queue)
            thread.start()
        for j in range(table_queue.qsize() % thread_count) :
            setting.setting_column_on_queue()
        #big_cat = selects.select_lv1_category(table)
        
        for j in range(thread_count) :

            thread = threading.Thread(target=setting.setting_column_on_queue_bit_cat)
            thread.start()

        for j in range(table_queue.qsize() % thread_count) :
            setting.setting_column_on_queue_bit_cat()

        '''
        huge_cat = []
        for i in big_cat :
            appending_ops = str(i).split("(")[0]
            if not appending_ops in huge_cat :
                huge_cat.append(appending_ops)
        print("sectors1 huge_cat :")
        prints.print_list(huge_cat)
        '''

        
        print("big_cat_queue.qsize() :",big_cat_queue.qsize())
        print("last_ops_queue.qsize() :",last_ops_queue.qsize())
        print("table_queue.qsize() :",table_queue.qsize())
        
        huge_cat = []
        for j in range(big_cat_queue.qsize()) :
            temp1 = big_cat_queue.get()
            huge_cat.append(temp1)
        huge_cat = set(huge_cat)
        huge_cat = list(huge_cat)
        huge_cat.sort()
        print("sector 1 huge_cat :")
        prints.print_list(huge_cat)
        
        print("before get while")

        print("1")
        frame=tkinter.Frame(root)

        scrollbar=tkinter.Scrollbar(frame)
        scrollbar.pack(side="right", fill="y")

        listbox=tkinter.Listbox(frame, width=50, height=20, yscrollcommand = scrollbar.set)
        listbox = prints.get_div_6_on_listbox(huge_cat,listbox)
        listbox.pack(side="right")

        scrollbar["command"]=listbox.yview

        frame.pack()

        prints.print_div_6(huge_cat)
        os.system("pause")
        user_big_cat = ""
        while True :
            print("종류를 정확히 골라주세요")
            user_big_cat = input("입력 :")
            if user_big_cat in huge_cat :
                print("주제가 정확히 들어맞음을 확인했습니다.")
                break
            else :
                print("주제가 포함되지 않음을 확인했습니다.")
                continue
        
        small_cat = selects.select_lv2_category(table,user_big_cat)
        print("sector 1 small_cat :")
        prints.print_list(small_cat)

        kinds_lv2 = []
        for i in table :
            if i[1] not in kinds_lv2 :
                kinds_lv2.append(i[1])
        print("duplicate_deficiencying kinds_lv2 :",kinds_lv2)
        prints.print_list(kinds_lv2)
        setting.sorting_grade(kinds_lv2)
        print("1.품목명별 정보 출력(기본값)")
        print("2.단위별 정보 출력")
        print("3.등급별 정보 출력")
        print("4.가격별 정보 출력")
        sorting_sub = input("입력 : ")
        kinds_res_cat = setting.duplicate_deficiencying_name(small_cat)
        kinds_res_cat = setting.integrating_list(kinds_res_cat)

        

        if sorting_sub== "1" :
            print("품목명별 정보 출력 선택됨")
        elif sorting_sub== "2" :
            print("단위별 정보 출력 선택됨")
            #kinds_res_cat.sort(key=lambda x:x[1])
            
        elif sorting_sub== "3" :
            print("등급별 정보 출력 선택됨")
            kinds_res_cat.sort(key=lambda x:x[2])
        elif sorting_sub== "4" :
            print("가격별 정보 출력 선택됨")
            kinds_res_cat.sort(key=lambda x:x[3])



        
        print("이름\t\t\t\t무게\t등급\t\t평균가격")
        for i in kinds_res_cat :
            #print("sector 1 kinds_res_cat i :",i)
            #print("{}\t\t{}\t{}\t\t{}".format(i[0][0],i[0][1],i[0][2],i[1]))
            #get_real_length_on_CMD
            pass
            print(i[0],end="")
            if prints.get_real_length_on_CMD(i[0]) < 8 :
                print("\t\t\t\t",end="")
            elif prints.get_real_length_on_CMD(i[0]) < 16 :
                print("\t\t\t",end="")
            elif prints.get_real_length_on_CMD(i[0]) < 24 :
                print("\t\t",end="")
            elif prints.get_real_length_on_CMD(i[0]) < 32 :
                print(" \t",end="")
                
            print(i[1],end="\t")
            print(i[2],end="")
            if prints.get_real_length_on_CMD(i[2]) < 8 :
                print("\t\t",end="")
            elif prints.get_real_length_on_CMD(i[2]) < 16 :
                print("\t",end="")
            print(i[3])
        print("이름\t\t\t\t무게\t등급\t\t평균가격")
        
        print("\n\n")
        print("sector 1 의 역할이 전부 끝났습니다.\n계속 하시려면 엔터, 그만두시려면 'ㄴ' 또는 's'를 눌러주세요")
        choose_exit = input("입력 : ")
        choose_exit.lower()
        print("\n\n")


thread_count = 12

root = tkinter.Tk()
cv_width = 800
cv_height = 400
canvas = tkinter.Canvas(width=cv_width,height= cv_height)
canvas.pack()
text = tkinter.Label(text="Hello world")
text.pack()
button = tkinter.Button(text = "1.품목명별 정보 출력", font = ("System", 32),width=20,height=1,command=sectors.sector1)
button.pack(side="top")
root.mainloop()