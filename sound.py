from playsound import playsound
karaoke_song_number = ""
characters = "ok"
while True:
    karaoke_song_number_num = str(input("노래방 노래 번호를 입력해주세요: "))
    print(karaoke_song_number_num)
    karaoke_song_number = karaoke_song_number + karaoke_song_number_num
    if karaoke_song_number_num == "1":
            playsound("sound/1.wav")
    if karaoke_song_number_num == "2":
            playsound("sound/2.wav")
    if karaoke_song_number_num == "3":
            playsound("sound/3.wav")
    if karaoke_song_number_num == "4":
            playsound("sound/4.wav")
    if karaoke_song_number_num == "5":
            playsound("sound/5.wav")
    if karaoke_song_number_num == "6":
            playsound("sound/6.wav")
    if karaoke_song_number_num == "7":
            playsound("sound/7.wav")
    if karaoke_song_number_num == "8":
            playsound("sound/8.wav")
    if karaoke_song_number_num == "9":
            playsound("sound/9.wav")
    if karaoke_song_number_num == "ok":
        for x in range(len(characters)):
                karaoke_song_number = karaoke_song_number.replace(characters[x],"")
        print(karaoke_song_number)
        break