s = '''Dusre ke pyaar Mai girne se tujhe bacha raha hu
Sab mujhe bhao de rahi 
Firbhi sabko wata raha hu
Tere baar mai sabko Achi baateh bata raha hu
Tere liye ghar pe mummy daddy ko Mai mana raha hu
Wazan meri thodi Ghata raha hu
Tujhe lean body pasand hai 
Mai healthy khaane chaba raha hu
Sunne Mai aaya hai tu London mai rehti hai
Abbi ke abbi jaake phehli ticket kata raha hu

(Rap 1)

Tu toh rapchick hai situation badi drastic hai 
Tera smile both hard baaki sabki plastic hai
Door khadhi achi nahi lagrahi tu mere pass theek hai 
Haath se khaata tha tere liye kharaha chopstick se 
Optic se alag alag chasma liya ghar phocha toh mom stick se maari mujhe sadma diya 
Boli ki tu pyaar mai nahi padhna lekin mai padhne laga tha 
Teri chaal sab kamal apsara yeh razor gaal 
Sab bawaal ho jayega mere saath reke dekh
Tujhe koi na milega pure raaste pe ek 
Banda mere jaisa, rehre kaisa jaisa teko chahiye tu bhi apne pe fida toh ek number sahi hai

(Rap 2)
Nazar nahi hatreli meri teri pe faseli 
Tu dimaag mai chapeli, kyuki tu pateli nahi karti baby auro ki tarha,
Mera aaj Abhi Aur tomorrow bhi tera 
Tere saamne mai seedha baki banda Mai tedha 
Sab kehte banna mat yeda 
Meko toh khaane ka peda 
Tera jo mera  mera jo Tera 
Ujala bhar daala tune toh andheraich nahi hai
Baasmati tukda nahi be lamba rice chahiye 
Apna life sahi hai sabka life sahi hai 
Jindagi ko sahi taur pe jeene wala chahiye
Jo bhi baat bola Maine sab baat sahi hai
Chodh dunga teko aisa koi shot nahi hai
'''
import win32com.client


speaker = win32com.client.Dispatch("SAPI.SpVoice")

speaker.Speak(s)    
