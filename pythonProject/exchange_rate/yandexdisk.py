import yadisk


# https://oauth.yandex.ru/authorize?response_type=token&client_id=27f8599278d1498c8e3d82b8a6da4204
def get_file_from_yadisk():
    y = yadisk.YaDisk(token="y0_AgAAAAAKNdTkAAsKBQAAAAD10buxJXImm5BFRn-x9cPfFUUXP_zZcv0")
    # Удаленние с диска перед загрузкой
    # y.remove("Текстовый документ.txt", permanently=True)
    # Загрузка на диск
    # y.upload("Текстовый документ.txt","/Текстовый документ.txt")
    # Загрузка с диска
    y.download("/Бюджет.xlsx", "Бюджет.xlsx")
    #
