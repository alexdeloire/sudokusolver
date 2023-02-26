import tkinter as tk

def SudokuReset():

    for i in range(9):
        for j in range(9):
            listvalue[i][j].set(0)
            listentry[i][j].configure(bg="white",font=("Calibri", 20))

    print("-- Grid Reset --")

def SetGrid1():	# Sudoku TP
    SudokuReset()
    sudoku=[]
    sudoku.append([0,5,0,4,0,0,0,0,0])
    sudoku.append([9,1,0,0,0,3,8,0,0])
    sudoku.append([0,0,3,0,1,0,0,0,7])
    sudoku.append([0,0,0,0,4,0,0,3,0])
    sudoku.append([7,0,1,6,0,8,4,0,2])
    sudoku.append([0,2,0,0,3,0,0,0,0])
    sudoku.append([1,0,0,0,9,0,5,0,0])
    sudoku.append([0,0,5,8,0,0,0,6,9])
    sudoku.append([0,0,0,0,0,4,0,2,0])

    for i in range(9):
        for j in range(9):
            listvalue[i][j].set(sudoku[i][j])
            if sudoku[i][j] != 0:
                # Set background color to grey if the value come from the start grid
                listentry[i][j].configure(bg="#E0E0E0")
                # Set font to bold instead of changing background color
                #listentry[i][j].configure(font=("Calibri", 20,"bold"))

    print("-- Config 1 --")

def SetGrid2():# Sudoku Enonce 2
    SudokuReset()
    sudoku=[]
    sudoku.append([3,0,0,4,1,0,0,8,7])
    sudoku.append([0,0,9,0,0,5,0,6,0])
    sudoku.append([4,0,0,7,9,0,5,0,3])
    sudoku.append([0,7,3,2,4,0,0,0,0])
    sudoku.append([0,0,0,0,0,0,0,0,0])
    sudoku.append([0,0,0,0,7,8,2,4,0])
    sudoku.append([6,0,2,0,8,3,0,0,5])
    sudoku.append([0,5,0,1,0,0,3,0,0])
    sudoku.append([1,3,0,0,2,4,0,9,6])

    for i in range(9):
        for j in range(9):
            listvalue[i][j].set(sudoku[i][j])
            if sudoku[i][j] != 0:
                # Set background color to grey if the value come from the start grid
                listentry[i][j].configure(bg="#E0E0E0")
                # Set font to bold instead of changing background color
                #listentry[i][j].configure(font=("Calibri", 20,"bold"))

    print("-- Config 2 --")

def SetGrid3():# Sudoku Easy
    SudokuReset()
    sudoku=[]
    sudoku.append([2,9,0,0,3,1,7,8,0])
    sudoku.append([0,1,6,0,0,0,0,2,4])
    sudoku.append([0,7,0,4,0,0,5,9,0])
    sudoku.append([4,0,0,0,0,0,8,6,5])
    sudoku.append([0,0,0,8,5,9,0,0,0])
    sudoku.append([7,8,5,0,0,0,0,0,2])
    sudoku.append([0,5,7,0,0,3,0,4,0])
    sudoku.append([8,2,0,0,0,0,1,7,0])
    sudoku.append([0,4,1,7,9,0,0,5,3])

    for i in range(9):
        for j in range(9):
            listvalue[i][j].set(sudoku[i][j])
            if sudoku[i][j] != 0:
                # Set background color to grey if the value come from the start grid
                listentry[i][j].configure(bg="#E0E0E0")
                # Set font to bold instead of changing background color
                #listentry[i][j].configure(font=("Calibri", 20,"bold"))

    print("-- Config 3 --")

def SetGrid4():# Sudoku Hard
    SudokuReset()
    sudoku=[]
    sudoku.append([7,2,0,4,0,6,0,0,3])
    sudoku.append([0,0,4,0,0,0,7,0,0])
    sudoku.append([0,5,0,0,0,0,0,2,0])
    sudoku.append([0,1,5,0,0,4,0,0,8])
    sudoku.append([0,0,0,2,0,7,0,0,0])
    sudoku.append([9,0,0,5,0,0,2,4,0])
    sudoku.append([0,6,0,0,0,0,0,1,0])
    sudoku.append([0,0,3,0,0,0,8,0,0])
    sudoku.append([5,0,0,1,0,8,0,9,4])

    for i in range(9):
        for j in range(9):
            listvalue[i][j].set(sudoku[i][j])
            if sudoku[i][j] != 0:
                # Set background color to grey if the value come from the start grid
                listentry[i][j].configure(bg="#E0E0E0")
                # Set font to bold instead of changing background color
                #listentry[i][j].configure(font=("Calibri", 20,"bold"))

    print("-- Config 4 --")

def StdoutPrint():
    print("-- Printing Sudoku Actual State --\n")
    for i in range(9):
        line = "     "
        if i % 3 == 0 and i != 0:
            print("      - - - - - - - - - - -")
        for j in range(9):
            if j % 3 == 0 and j != 0:
                line += " |"
            line = line + " " + str(listvalue[i][j].get())
        print(line)
    print("\nSolved!\n")

# Counts the number of iterations
compteur=0

def RunButton2():
    #This button solves the Sudoku with less iterations the RunV1
    global compteur
    print("Solving Sudoku")

    #Exercice 1
    
    def missing(liste):
      liste_missing=[]
      for i in range(1,10):
          if i not in liste:
            liste_missing.append(i)
      return liste_missing
    
    #Exercice 2
    
    def missing_ligne(grille,num_ligne):
        return missing(grille[num_ligne])
    
    #Exercice 3
    
    def missing_colonne(grille,num_colonne):
        return missing([ligne[num_colonne] for ligne in grille])
    
    #Exercice 4
    
    def missing_region(grille,num_ligne,num_colonne):
        region_ligne,region_colonne=num_ligne//3,num_colonne//3
        liste_region=[]
        for i in range(region_ligne*3,(region_ligne*3)+3):
            for j in range(region_colonne*3,(region_colonne*3)+3):
                liste_region.append(grille[i][j])
        return missing(liste_region)
    
    #Exercice 5
    
    def valeurs_communes(l1,l2):
        liste_val_commun=[] #resultat a retourner
        for i in l1:
            if i in l2:
                liste_val_commun.append(i)
        return liste_val_commun
    
    def valeurs_possibles_case(grille,num_ligne,num_colonne):
        liste_region=missing_region(grille,num_ligne,num_colonne)
        liste_ligne=missing_ligne(grille,num_ligne)
        liste_colonne=missing_colonne(grille,num_colonne)
        return valeurs_communes(valeurs_communes(liste_ligne,liste_colonne),liste_region)
    
    #Exercice 6
    
    def listePositionsNonRemplies(grille):
        liste_cases=[]
        for i in range(9):
            for j in range(9):
                if grille[i][j]==0:
                    liste_cases.append((i,j))
        return liste_cases
    
    #Exercice 7

    def case_avec_mini(grille,lpos):
      liste=[]
      for i in lpos:
          liste.append((i,len(valeurs_possibles_case(grille,i[0],i[1]))))
      min=liste[0]
      for i in liste:
          if i[1]<=min[1]:
              min=i
      return min[0]

    def supprime_ele(liste,x):
        k="salut"
        for i in range(len(liste)):
            if liste[i]==x:
                #print(("true"))  #un test j'avais des bug
                k=i
              
        return liste[:k]+liste[k+1:]
    
    def grillefinie1(grille,lpos):
        global compteur
        compteur=compteur+1
        if len(lpos)==0:
            return grille, True
        else:
            tuple_lig_col=case_avec_mini(grille,lpos)
            liste_valeurs=valeurs_possibles_case(grille,tuple_lig_col[0],tuple_lig_col[1])
            lpos=supprime_ele(lpos,tuple_lig_col)
            for i in liste_valeurs:
                #grillecopy=deepcopy(grille)
                #grillecopy[tuple_lig_col[0]][tuple_lig_col[1]]=i
                grille[tuple_lig_col[0]][tuple_lig_col[1]]=i
                #lpos=supprime_ele(lpos,tuple_lig_col)
                grillenew,valeurbool = grillefinie1(grille,lpos) #ou grillecopy
                if valeurbool:
                    return grillenew,True
            #pas besoin de rajouter dans lpos
            #print("remettre 0 a",tuple_lig_col)
            grille[tuple_lig_col[0]][tuple_lig_col[1]]=0
            return grille,False
    
    
    def sudoku1(grille):
        lpos=listePositionsNonRemplies(grille)
        #print(lpos)
        if len(lpos) > 0:
            return grillefinie1(grille,lpos)
        else: 
            return (grille,False)


    grilleinter=[[0 for i in range(9)] for j in range(9)]
    for i in range(9):
      for j in range(9):
        grilleinter[i][j]=listvalue[i][j].get()
    #print(grilleinter)
    grilleinter=sudoku1(grilleinter)[0]
    for i in range(9):
      for j in range(9):
        #print(grilleinter[i][j])
        listvalue[i][j].set(grilleinter[i][j])
    StdoutPrint()
    print("Nombre d'itérations:",compteur)
    compteur=0


def RunButton1():
    # Button that solves Sudoku
    global compteur
    print("Solving Sudoku")

    #Exercice 1
    
    def missing(liste):
      liste_missing=[]
      for i in range(1,10):
          if i not in liste:
            liste_missing.append(i)
      return liste_missing
    
    #Exercice 2
    
    def missing_ligne(grille,num_ligne):
        return missing(grille[num_ligne])
    
    #Exercice 3
    
    def missing_colonne(grille,num_colonne):
        return missing([ligne[num_colonne] for ligne in grille])
    
    #Exercice 4
    
    def missing_region(grille,num_ligne,num_colonne):
        region_ligne,region_colonne=num_ligne//3,num_colonne//3
        liste_region=[]
        for i in range(region_ligne*3,(region_ligne*3)+3):
            for j in range(region_colonne*3,(region_colonne*3)+3):
                liste_region.append(grille[i][j])
        return missing(liste_region)
    
    #Exercice 5
    
    def valeurs_communes(l1,l2):
        liste_val_commun=[] #resultat a retourner
        for i in l1:
            if i in l2:
                liste_val_commun.append(i)
        return liste_val_commun
    
    def valeurs_possibles_case(grille,num_ligne,num_colonne):
        liste_region=missing_region(grille,num_ligne,num_colonne)
        liste_ligne=missing_ligne(grille,num_ligne)
        liste_colonne=missing_colonne(grille,num_colonne)
        return valeurs_communes(valeurs_communes(liste_ligne,liste_colonne),liste_region)
    
    #Exercice 6
    
    def listePositionsNonRemplies(grille):
        liste_cases=[]
        for i in range(9):
            for j in range(9):
                if grille[i][j]==0:
                    liste_cases.append((i,j))
        return liste_cases
    
    #Exercice 7
    
    def grillefinie(grille,lpos,index):
        global compteur
        compteur=compteur+1
        if index >= len(lpos):
            return grille, True
        else:
            tuple_lig_col=lpos[index]
            liste_valeurs=valeurs_possibles_case(grille,tuple_lig_col[0],tuple_lig_col[1])
            for i in liste_valeurs:
                #grillecopy=deepcopy(grille)
                #grillecopy[tuple_lig_col[0]][tuple_lig_col[1]]=i
                grille[tuple_lig_col[0]][tuple_lig_col[1]]=i
                grillenew,valeurbool = grillefinie(grille,lpos,index+1) #ou grillecopy
                if valeurbool:
                    return grillenew,True
            # On travaille par référence en python
            grille[tuple_lig_col[0]][tuple_lig_col[1]]=0      
            return grille,False
    
    
    def sudoku(grille):
        lpos=listePositionsNonRemplies(grille)
        if len(lpos) > 0:
            return grillefinie(grille,lpos,0)
        else: 
            return (grille,False)

    grilleinter=[[0 for i in range(9)] for j in range(9)]
    for i in range(9):
      for j in range(9):
        grilleinter[i][j]=listvalue[i][j].get()
    #print(grilleinter)
    grilleinter=sudoku(grilleinter)[0]
    for i in range(9):
      for j in range(9):
        #print(grilleinter[i][j])
        listvalue[i][j].set(grilleinter[i][j])
    StdoutPrint()
    print("Nombre d'itérations:",compteur)
    compteur=0

  
### Window creation
window = tk.Tk()


### Printing Title
title = tk.Label(window, text="My Sudoku Solver", font=("Calibri", 30), justify="center").grid(row=1, column=0, columnspan=20)

### Empty grid of sudoku, 0 in all boxes
listvalue = [[tk.IntVar() for j in range(9)] for i in range(9)]
listentry = [[0 for j in range(9)] for i in range(9)]
### Assigning boxes to Interactive Grid
for ligne in range(9):
    for colonne in range(9):
        listentry[ligne][colonne]=tk.Entry(
            window,
            textvariable=listvalue[ligne][colonne],
            width=2,
            relief="raised",
            font=("Calibri", 20),
            justify="center",
        )
        listentry[ligne][colonne].grid(row=(ligne + 1) * 2, column=(colonne + 1) * 2)

### Exemple Config 

tk.Button(window, text="Grid 1", command=SetGrid1).grid(row=2, column=20, rowspan=2)
tk.Button(window, text="Grid 2", command=SetGrid2).grid(row=4, column=20, rowspan=2)
tk.Button(window, text="Grid 3", command=SetGrid3).grid(row=5, column=20, rowspan=2)
tk.Button(window, text="Grid 4", command=SetGrid4).grid(row=7, column=20, rowspan=2)

### Button Config
tk.Button(window, text="RunV1", command=RunButton1).grid(row=20, column=2, columnspan=3)
tk.Button(window, text="Reset", command=SudokuReset).grid(row=20, column=16, columnspan=3)
tk.Button(window, text="Close", command=window.quit).grid(row=20, column=20, columnspan=3)
tk.Button(window, text="RunV2", command=RunButton2).grid(row=20, column=6, columnspan=3)

### Border Layout
tk.Label(window, text="", fg="blue4", bg="#404040").grid(row=2, column=7, rowspan=17, sticky="ns")
tk.Label(window, text="", fg="blue4", bg="#404040").grid(row=2, column=13, rowspan=17, sticky="ns")

tk.Label(window, text="", fg="blue4", bg="#404040", font=("Calibri", 1)).grid(row=7, column=2, columnspan=17, sticky="ew")
tk.Label(window, text="", fg="blue4", bg="#404040", font=("Calibri", 1)).grid(row=13, column=2, columnspan=17, sticky="ew")

window.grid_rowconfigure(0, minsize=10)
window.grid_rowconfigure(19, minsize=10)
window.grid_rowconfigure(21, minsize=10)
window.grid_columnconfigure(0, minsize=10)
window.grid_columnconfigure(19, minsize=10)
window.grid_columnconfigure(21, minsize=10)

### Loop
window.mainloop()

print("Window Closed, End of Program\nBye !")