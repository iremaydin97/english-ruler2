#İstenilen sayıda ekrana tire yazan fonksiyon
def draw_line(tick_length, tick_label=''):   
    line = '-' * tick_length
    if tick_label:
        line += ' ' + tick_label
    print(line)

#Belirlenen merkez noktasına göre ara uzunlukların yazdırıldığı fonksiyon. 
def draw_interval(center_length):
        if center_length > 0:  # Merkez noktasının 0 dan büyük olduğu durumlarda.
        draw_interval(center_length - 1) #merkez noktanın üstünde kalan tireler çizilir. 
        draw_line(center_length)  # Merkez noktasının tireleri çizilir.
        draw_interval(center_length - 1)  # Merkez noktasının altında kalan tireler çizilir.


#İstenilen tire sayısı ve inç uzunluğu ile cetvel çizme metodu.
def draw_ruler(num_inches, major_length):
    draw_line(major_length, '0')  # Başlangıç noktası.
#Bir for döngüsü oluşturularak girilen sayı bazında ana ve ara tireler çizilecek.
    for j in range(1, 1 + num_inches):
        draw_interval(major_length - 1)  #inç için iç tireler çizilir.
        draw_line(major_length, str(j))  # inç j hattı çizilir ve adlandırılır.



    draw_ruler(1, 4) # 1 inçlik 4 tireli cetvel.
    print('=' * 30)
    draw_ruler(1, 5) # 1 inçlik 5 tireli cetvel.
    print('=' * 30)
    draw_ruler(1, 3) # 1 inçlik 3 tireli cetvel.