class students:
    def __init__(self, name, usn, branch, sem,gender,):
        self.name = name
        self.usn= usn
        self.branch= branch
        self.sem= sem
        self.gender= gender

    def get_details(self):
        print(f"Name: {self.name}, USN: {self.usn}, Branch: {self.branch}, Semester: {self.sem}, Gender: {self.gender}")
# Create student objects
AAFIYA = students("AAFIYA","1SV24AI001","AIML",3,"FEMALE")
ABHILASH = students("ABHILASH","1SV24AI002","AIML",3,"MALE")
AMULYA_E = students("AMULYA E","1SV24AI003","AIML",3,"FEMALE")
ANURAG_S_BEDRE = students("ANURAG S BEDRE","1SV24AI004","AIML",3,"MALE")
ARBIYA_BANU = students("ARBIYA BANU","1SV24AI005","AIML",3,"FEMALE")    
BHOOMIKA_T = students("BHOOMIKA T","1SV24AI006","AIML",3,"FEMALE")  
CHANDRASEKHAR_K = students("CHANDRASEKHAR K","1SV24AI007","AIML",3,"MALE")
CHARANKUMAR_C_GANIGER = students("CHARANKUMAR C GANIGER","1SV24AI008","AIML",3,"MALE")
D_MANJULA = students("D MANJULA","1SV24AI009","AIML",3,"FEMALE")
DARSHAN_PL = students("DARSHAN PL","1SV24AI010","AIML",3,"MALE")
DHANALAKSHMI_R = students("DHANALAKSHMI S","1SV24AI011","AIML",3,"FEMALE")
DIVYA_N = students("DIVYA N","1SV24AI012","AIML",3,"FEMALE")
DIVYASHREE_N_V = students("DIVYASHREE N V","1SV24AI013","AIML",3,"FEMALE")
EILEEN_PRASAD = students("EILEEN PRASAD","1SV24AI014","AIML",3,"FEMALE")
FIZA = students("FIZA","1SV24AI015","AIML",3,"FEMALE")
GANESH_R_KULKARNI = students("GANESH R KULKARNI","1SV24AI016","AIML",3,"MALE")
GURUNATH_PRASHANT_BANKAPUR = students("GURUNATH PRASHANT BANKAPUR","1SV24AI017","AIML",3,"MALE")
H_M_GANESH = students("H M GANESH","1SV24AI018","AIML",3,"MALE")
J_BHUVANESH = students("J BHUVANESH","1SV24AI019","AIML",3,"MALE")
JEEVAN_REDDY = students("JEEVAN REDDY","1SV24AI020","AIML",3,"MALE")
KAIVALYA_REDDY_Y_P = students("KAIVALYA REDDY Y P","1SV24AI021","AIML",3,"MALE")
KANTESH_BIJAPUR = students("KANTESH BIJAPUR","1SV24AI022","AIML",3,"MALE")
LAXMI_KURUVATTIGOUDA = students("LAXMI KURUVATTIGOUDA ","1SV24AI023","AIML",3,"FEMALE")
LIKHITHA_N = students("LIKHITHA N","1SV24AI024","AIML",3,"FEMALE")
M_THRUPTHI = students("M THRUPTHI","1SV24AI025","AIML",3,"FEMALE")
MALLIKARJUN_IRAPPA_CHITTI = students("MALLIKARJUN IRAPPA CHITTI","1SV24AI026","AIML",3,"MALE")
MALLIKARJUN_SIDDAPPA = students("MALLIKARJUN SIDDAPPA","1SV24AI027","AIML",3,"MALE")
NIKHIL_H_O = students("NIKHIL H O","1SV24AI028","AIML",3,"MALE")
NITIN_S = students("NITIN S","1SV24AI029","AIML",3,"MALE")
PRAJWAL_S_S = students("PRAJWAL S S","1SV24AI030","AIML",3,"MALE")
RAHUL_G = students("RAHUL G","1SV24AI031","AIML",3,"MALE")
RAHUL_P = students("RAHUL P","1SV24AI032","AIML",3,"MALE")
RAKSHITHA_D_J = students("RAKSHITHA D J","1SV24AI033","AIML",3,"FEMALE")
RAZIYA_SULTANA = students("RAZIYA SULTANA","1SV24AI034","AIML",3,"FEMALE")
RUMAN_K = students("RUMAN K","1SV24AI035","AIML",3,"MALE")
S_J_GANESHGOUDA = students("S J GANESHGOUDA","1SV24AI036","AIML",3,"MALE")
SADASHIV_SANTOSHKUMAR = students("SADASHIV SANTOSHKUMAR","1SV24AI037","AIML",3,"MALE")
SHAIK_MOHAMMED_NAQEEB = students("SHAIK MOHAMMED NAQEEB","1SV24AI038","AIML",3,"MALE")
SHARANYA_N_R = students("SHARANYA N R","1SV24AI039","AIML",3,"FEMALE")
SHASHANK_M_L = students("SHASHANK M L","1SV24AI040","AIML",3,"MALE")
SIDDALINGAYYA_R_ARADANAMAT = students("SIDDALINGAYYA R ARADANAMAT","1SV24AI041","AIML",3,"MALE")
SIDDESHWAR_SURESH_HEGALE = students("SIDDESHWAR SURESH HEGALE","1SV24AI042","AIML",3,"MALE")
SRUJAN_R_P = students("SRUJAN R P","1SV24AI043","AIML",3,"MALE")
SUFIYA_KOUSER = students("SUFIYA KOUSER","1SV24AI044","AIML",3,"FEMALE")
SUKANYA_SHRISHAILA = students("SUKANYA SHRISHAILA","1SV24AI045","AIML",3,"FEMALE")
VIKAS_AWATI = students("VIKAS AWATI","1SV24AI046","AIML",3,"MALE")
VINAYAKA_V = students("VINAYAKA V","1SV24AI047","AIML",3,"MALE")    
DHANUSH_R = students("DHANUSH R","LE","AIML",3,"MALE")
M_VIJAYKUMAR = students("M VIJAYKUMAR","LE","AIML",3,"MALE")
PRIYA_K_M = students("PRIYA K M","LE","AIML",3,"FEMALE")
RANJITHA_P = students("RANJITHA P","LE","AIML",3,"FEMALE")
THARUN_KUMAR_G = students("THARUN KUMAR G","LE","AIML",3,"MALE")

name = input("Enter the name of the student: ").lower()
if name == "aafiya":
    AAFIYA.get_details()
elif name == "abhilash":
    ABHILASH.get_details() 
elif name == "amulya e":
    AMULYA_E.get_details()
elif name == "anurag s bedre":
    ANURAG_S_BEDRE.get_details()
elif name == "arbiya banu":
    ARBIYA_BANU.get_details()
elif name == "bhoomika t":
    BHOOMIKA_T.get_details()
elif name == "chandrasekhar k":
    CHANDRASEKHAR_K.get_details()
elif name == "charankumar c ganiger":
    CHARANKUMAR_C_GANIGER.get_details()
elif name == "d manjula":
    D_MANJULA.get_details()
elif name == "darshan pl":
    DARSHAN_PL.get_details()
elif name == "dhanalakshmi r":
    DHANALAKSHMI_R.get_details()
elif name == "divya n":
    DIVYA_N.get_details()
elif name == "divyashree n v":
    DIVYASHREE_N_V.get_details()
elif name == "eileen prasad":
    EILEEN_PRASAD.get_details()
elif name == "fiza":
    FIZA.get_details()
elif name == "ganesh r kulkarni":
    GANESH_R_KULKARNI.get_details()
elif name == "gurunath prashant bankapur":
    GURUNATH_PRASHANT_BANKAPUR.get_details()
elif name == "h m ganesh":
    H_M_GANESH.get_details()
elif name == "j bhuvanesh":
    J_BHUVANESH.get_details()
elif name == "jeevan reddy":
    JEEVAN_REDDY.get_details()
elif name == "kaivalya reddy y p":
    KAIVALYA_REDDY_Y_P.get_details()
elif name == "kantesh bijapur":
    KANTESH_BIJAPUR.get_details()
elif name == "laxmi kuruvattigouda ":
    LAXMI_KURUVATTIGOUDA.get_details()
elif name == "likhitha n":
    LIKHITHA_N.get_details()
elif name == "m thrupthi":
    M_THRUPTHI.get_details()
elif name == "mallikarjun irappa chitti":
    MALLIKARJUN_IRAPPA_CHITTI.get_details()
elif name == "mallikarjun siddappa":
    MALLIKARJUN_SIDDAPPA.get_details()
elif name == "nikhil h o":
    NIKHIL_H_O.get_details()
elif name == "nitin s":
    NITIN_S.get_details()
elif name == "prajwal s s":
    PRAJWAL_S_S.get_details()
elif name == "rahul g":
    RAHUL_G.get_details()
elif name == "rahul p":
    RAHUL_P.get_details()
elif name == "rakshitha d j":
    RAKSHITHA_D_J.get_details()
elif name == "raziya sultana":
    RAZIYA_SULTANA.get_details()
elif name == "ruman k":
    RUMAN_K.get_details()
elif name == "s j ganeshgouda":
    S_J_GANESHGOUDA.get_details()
elif name == "sadashiv santoshkumar":
    SADASHIV_SANTOSHKUMAR.get_details()
elif name == "shaik mohammed naqeeb":
    SHAIK_MOHAMMED_NAQEEB.get_details()
elif name == "sharanya n r":
    SHARANYA_N_R.get_details()
elif name == "shashank m l":
    SHASHANK_M_L.get_details()
elif name == "siddalingayya r aradanamat":
    SIDDALINGAYYA_R_ARADANAMAT.get_details()
elif name == "siddeshwar suresh hegale":
    SIDDESHWAR_SURESH_HEGALE.get_details()
elif name == "srujan r p":
    SRUJAN_R_P.get_details()
elif name == "sufiya kouser":
    SUFIYA_KOUSER.get_details()
elif name == "sukanya shrishaila":
    SUKANYA_SHRISHAILA.get_details()
elif name == "vikas awati":
    VIKAS_AWATI.get_details()
elif name == "vinayaka v":
    VINAYAKA_V.get_details()
elif name == "dhanush r":
    DHANUSH_R.get_details()
elif name == "m vijaykumar":
    M_VIJAYKUMAR.get_details()
elif name == "priya k m":
    PRIYA_K_M.get_details()
elif name == "ranjitha p":
    RANJITHA_P.get_details()
elif name == "tharun kumar g":
    THARUN_KUMAR_G.get_details()
else:
    print("Student not found.")

import tkinter as tk
from tkinter import messagebox
root = tk.Tk()
root.title("College Student")
root.geometry("400x300")
root.config(bg="#f0f4f7")
def search_student():
    name = entry_name.get().lower()
    student_dict = {
        "1sv24ai001": AAFIYA,
        "1sv24ai002": ABHILASH,
        "1sv24ai003": AMULYA_E,
        "1sv24ai004": ANURAG_S_BEDRE,
        "1sv24ai005": ARBIYA_BANU,
        "1sv24ai006": BHOOMIKA_T,
        "1sv24ai007": CHANDRASEKHAR_K,
        "1sv24ai008": CHARANKUMAR_C_GANIGER,
        "1sv24ai009": D_MANJULA,
        "1sv24ai010": DARSHAN_PL,
        "1sv24ai011": DHANALAKSHMI_R,
        "1sv24ai012": DIVYA_N,
        "1sv24ai013": DIVYASHREE_N_V,
        "1sv24ai014": EILEEN_PRASAD,
        "1sv24ai015": FIZA,
        "1sv24ai016": GANESH_R_KULKARNI,
        "1sv24ai017": GURUNATH_PRASHANT_BANKAPUR,
        "1sv24ai018": H_M_GANESH,
        "1sv24ai019": J_BHUVANESH,
        "1sv24ai020": JEEVAN_REDDY,
        "1sv24ai021": KAIVALYA_REDDY_Y_P,
        "1sv24ai022": KANTESH_BIJAPUR,
        "1sv24ai023": LAXMI_KURUVATTIGOUDA,
        "1sv24ai024": LIKHITHA_N,
        "1sv24ai025": M_THRUPTHI,
        "1sv24ai026": MALLIKARJUN_IRAPPA_CHITTI,
        "1sv24ai027": MALLIKARJUN_SIDDAPPA,
        "1sv24ai028": NIKHIL_H_O,
        "1sv24ai029": NITIN_S,
        "1sv24ai030": PRAJWAL_S_S,
        "1sv24ai031": RAHUL_G,
        "1sv24ai032": RAHUL_P,
        "1sv24ai033": RAKSHITHA_D_J,
        "1sv24ai034": RAZIYA_SULTANA,
        "1sv24ai035": RUMAN_K,
        "1sv24ai036": S_J_GANESHGOUDA,
        "1sv24ai037": SADASHIV_SANTOSHKUMAR,
        "1sv24ai038": SHAIK_MOHAMMED_NAQEEB,
        "1sv24ai039": SHARANYA_N_R,
        "1sv24ai040": SHASHANK_M_L,
        "1sv24ai041": SIDDALINGAYYA_R_ARADANAMAT,
        "1sv24ai042": SIDDESHWAR_SURESH_HEGALE,
        "1sv24ai043": SRUJAN_R_P,
        "1sv24ai044": SUFIYA_KOUSER,
        "1sv24ai045": SUKANYA_SHRISHAILA,
        "1sv24ai047": VIKAS_AWATI,
        "1sv24ai048": VINAYAKA_V,
        "dhanush r": DHANUSH_R,
        "m vijaykumar": M_VIJAYKUMAR,
        "priya k m": PRIYA_K_M,
        "ranjitha p": RANJITHA_P,
        "tharun kumar g": THARUN_KUMAR_G
    }
    student = student_dict.get(name)
    if student:
        output_label.config(text=f"Name: {student.name}\nUSN: {student.usn}\nBranch: {student.branch}\nSemester: {student.sem}\nGender: {student.gender}")
    else:
        messagebox.showerror("Error", "Student not found.")
        # Title
title_label = tk.Label(root, text="🎓 Student Information System", font=("Arial", 16, "bold"), bg="#f0f4f7", fg="#333")
title_label.pack(pady=10)

# Input Frame
input_frame = tk.Frame(root, bg="#f3f7f0")
input_frame.pack(pady=10)

tk.Label(input_frame, text="Enter Student Name:", font=("Arial", 12), bg="#f0f4f7").grid(row=0, column=0, padx=5)
entry_name = tk.Entry(input_frame, width=30, font=("Arial", 12))
entry_name.grid(row=0, column=1, padx=5)

# Search Button
search_btn = tk.Button(root, text="🔍 Search", font=("Arial", 12, "bold"), bg="#0078D7", fg="white", padx=10, pady=5, command=search_student)
search_btn.pack(pady=10)

# Output Label
output_label = tk.Label(root, text="", font=("Arial", 12), bg="#f0f4f7", fg="#222", justify="left")
output_label.pack(pady=15)

# Run App
root.mainloop()