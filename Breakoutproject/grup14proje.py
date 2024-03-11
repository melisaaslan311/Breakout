
"""
File: project.py
-----------------
This program is an empty program for your final project.  Update this comment
with a summary of your program!
"""

from graphics import Canvas
import random
import time


BAMBU_SAYISI=7
CAN_SAYISI=6
CANVAS_WIDTH = 1000
CANVAS_HEIGHT = 500
YUVA_SIZE = 150
ENGEL_SIZE = 75 
BAMBU_SIZE= 40
DELAY = 0.0005
ARADAKI_BOSLUK= 125
TOP_SIZE = 50
PANDA_SIZE= 50

def main():
    canvas = Canvas(CANVAS_WIDTH,CANVAS_HEIGHT)
    click=canvas.create_text(100,CANVAS_HEIGHT- 40 ,' baslamak icin buraya tiklayiniz')
    canvas.set_canvas_background_color('pink')
    canvas.wait_for_click()
    canvas.delete(click) 
    canvas.set_canvas_background_color('honeydew2')
    yuva(canvas)
    oyun_mekanigi(canvas, yuva, CAN_SAYISI )
    canvas.mainloop()
    
def yuva(canvas):
    panda_evi= canvas.create_image_with_size(0,0,YUVA_SIZE,YUVA_SIZE, 'yuva.jpg')
    return 
        
def oyun_mekanigi(canvas, yuva, CAN_SAYISI):
     
            ##pandanın yapımı
    panda=canvas.create_oval(0,CANVAS_HEIGHT-PANDA_SIZE,PANDA_SIZE, CANVAS_HEIGHT)
    canvas.set_color(panda, 'light blue')
    # panda= canvas.create_image(0,CANVAS_HEIGHT-PANDA_SIZE, 'pandaa.jpg')
   
   ## üstteki engelleri içine alan liste ve alttaki agacları içine alan liste olusturma 
       
    engel_ust_listesi=[]
    for i in range(4):
        x= 2* ARADAKI_BOSLUK+i*(ARADAKI_BOSLUK+ ENGEL_SIZE)
        agac = canvas.create_image(x,0, 'engel.jpg')
        canvas.set_color(agac, 'green')
        engel_ust_listesi.append(agac)
    
    
    engel_alt_listesi=[]
    for i in range(5):
        x2= ARADAKI_BOSLUK+ i*(ARADAKI_BOSLUK+ENGEL_SIZE)
        y1= CANVAS_HEIGHT- 2*ENGEL_SIZE
        agac1=canvas.create_image(x2,y1, 'engel.jpg') 
        engel_alt_listesi.append(agac1)
  
# ______________
   
     ##ileri geri gelen iki tane topu yaratma
   
    top2=canvas.create_oval(0,2*ENGEL_SIZE,TOP_SIZE,2*ENGEL_SIZE+TOP_SIZE)
    canvas.set_color(top2,'red1')
    top3 = canvas.create_oval(CANVAS_WIDTH-TOP_SIZE,CANVAS_HEIGHT/2 -TOP_SIZE,CANVAS_WIDTH,CANVAS_HEIGHT/2)
    canvas.set_color(top3,'red2')   
      
# ______________
     
       ## topların rastgele hareketi
    
    top2_hareket = random.randint(16,20)
    top3_hareket= random.randint(17,24)
       
# ______________
       
    ## icine asagıdakı ve ustteki bambuları alan listeleri yaratmak
    
    
    bambular_listesi_alt= []
    for i in range(5):
        x = (BAMBU_SIZE + (i+1)*(ARADAKI_BOSLUK+ENGEL_SIZE))
        bamb = canvas.create_image(x, CANVAS_HEIGHT- 2*BAMBU_SIZE, 'bambu.jpg')
        bambular_listesi_alt.append(bamb)
    
    bambular_listesi_ust= []
    for i in range(3):
        x = BAMBU_SIZE+ARADAKI_BOSLUK+ (i+1)*(ARADAKI_BOSLUK+ENGEL_SIZE)
        bambu= canvas.create_image(x,0,'bambu.jpg')
        bambular_listesi_ust.append(bambu)
    
      
#______________
    
   ##  toplanılan bambu sayısını sayan bir sayaç yaratma ve hak etiketi yaratma
    
    
    bambusayi=0
    hak_etiketi = canvas.create_text(canvas.get_canvas_width() - 30,
                                     canvas.get_canvas_height() - 30, str(CAN_SAYISI))
    canvas.set_font(hak_etiketi, "Arial", 20)
      
#______________
    
        # oyunun kuralları,  oyunu oynama

    oyun_bitti = False

    while not oyun_bitti:
        newx=canvas.get_mouse_x()
        newy=canvas.get_mouse_y()
        hareket=canvas.moveto(panda,newx- PANDA_SIZE/2 ,newy- PANDA_SIZE/2)
        canvas.move(top2,top2_hareket,0)
        canvas.move(top3,top3_hareket,0)
        clicks= canvas.get_new_mouse_clicks()
        for click in clicks:
            obje= canvas.find_element_at(click.x, click.y) 
            if obje in bambular_listesi_alt or obje in bambular_listesi_ust :
               canvas.delete(obje) 
               bambusayi+=1
               
    
         ## topların sekip ileri geri gitmesini saglayan emir
         
        if canvas.get_left_x(top2) >= CANVAS_WIDTH-TOP_SIZE or canvas.get_left_x(top2) <=0:
           top2_hareket= - top2_hareket
        if canvas.get_left_x(top3) >= CANVAS_WIDTH- TOP_SIZE/2 or canvas.get_left_x(top3) <=0:
           top3_hareket= - top3_hareket
     
    
            ## hak sayısının eksilme kosulu
            
        ## pandanın koordinatlarını bulmak ve panda eger engele degıyorsa veya toplara degıyorsa canı eksiltmek
        ## eger engele degerse candan bir eksilir toplara degme olursa ise candan iki eksilir, panda disariya cikarsa candan yine bir eksilir
            
        panda_koor= canvas.coords(panda)
        panda_sol_x = panda_koor[0]
        panda_ust_y = panda_koor[1]
        panda_alt_x = panda_koor[2]
        panda_alt_y = panda_koor[3]  
        top2_koor= canvas.coords(top2)
        top3_koor= canvas.coords(top3) 
     
        list_panda = canvas.find_overlapping(panda_sol_x, panda_ust_y, panda_alt_x, panda_alt_y)
        
        list_top2 = canvas.find_overlapping(top2_koor[0], top2_koor[1],
                                                        top2_koor[2], top2_koor[3]) 
        
        list_top3 = canvas.find_overlapping(top3_koor[0], top3_koor[1],
                                                        top3_koor[2], top3_koor[3])
       
    
        for pnd in list_panda :
            if pnd in engel_alt_listesi or pnd in engel_ust_listesi :
                CAN_SAYISI-=1                
                canvas.set_text(hak_etiketi, str(CAN_SAYISI))    
                if CAN_SAYISI>=0:
                  yazi= canvas.create_text(60,CANVAS_HEIGHT- 20 ,' oyuna devam etmek '+ '\n' + ' icin tiklayiniz')
                  click2= canvas.wait_for_click()
                  canvas.delete(yazi)
                  canvas.delete(click2)
                  
        for pnd in list_panda:
            if pnd in list_top2 :
                CAN_SAYISI-=1                
                canvas.set_text(hak_etiketi, str(CAN_SAYISI))    
                if CAN_SAYISI>=0:
                  yazi1= canvas.create_text(60,CANVAS_HEIGHT- 20 ,' oyuna devam etmek '+ '\n' + ' icin tiklayiniz')
                  click3= canvas.wait_for_click()
                  canvas.delete(yazi1)
                  canvas.delete(click3)
                  
                  
        for pnd in list_panda:
            if pnd in list_top3 :
                CAN_SAYISI-=1                
                canvas.set_text(hak_etiketi, str(CAN_SAYISI))    
                if CAN_SAYISI>=0:
                  yazi2= canvas.create_text(60,CANVAS_HEIGHT- 20 ,' oyuna devam etmek '+ '\n' + ' icin tiklayiniz')
                  click4= canvas.wait_for_click()
                  canvas.delete(yazi2)
                  canvas.delete(click4)
                  
                  
                  
        if newy <=0 or newx >= CANVAS_WIDTH-PANDA_SIZE/2 or newy >= CANVAS_HEIGHT- PANDA_SIZE/2 or newx <= 0 :
            CAN_SAYISI-=1                
            canvas.set_text(hak_etiketi, str(CAN_SAYISI))    
            if CAN_SAYISI>=0:
              yazi= canvas.create_text(60,CANVAS_HEIGHT- 20 ,' oyuna devam etmek '+ '\n' + ' icin tiklayiniz')
              click2= canvas.wait_for_click()
              canvas.delete(yazi)
              canvas.delete(click2)
              
          ## oyunu kazanma kosulu
             
        if bambusayi == 7 and newx < YUVA_SIZE and newy< YUVA_SIZE :
             oyun_bitti = True
             canvas.delete_all()
             oyun_bitti_etiketi = canvas.create_text(canvas.get_canvas_width() / 2,
                                                     canvas.get_canvas_height() / 2,
                                                  "YOU WIN!")
             canvas.set_font(oyun_bitti_etiketi, "Arial", 50)
             canvas.set_color(oyun_bitti_etiketi, "black")
             
          ## oyunu kazanma kosulu
        if CAN_SAYISI<= 0:
             oyun_bitti = True
             canvas.delete_all()
             oyun_bitti_etiketi = canvas.create_text(canvas.get_canvas_width() / 2,
                                                     canvas.get_canvas_height() / 2,
                                                   "GAME OVER!")
             canvas.set_font(oyun_bitti_etiketi, "Arial", 50)
             canvas.set_color(oyun_bitti_etiketi, "black")
                
               
        canvas.update()
        time.sleep(DELAY)

if __name__ == '__main__':
    main()