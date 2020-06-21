#프로그램명 : game_over
#작성자 : 오기탁
#조명 : 하이파이
#게임 오버를 구현하는 함수입니다
#텍스트를 출력하고 메인으로 돌아가거나 게임을 재시작합니다.

#setting.py에 정의된 colors입니다
colors = [(255, 102, 99), (158, 193, 207)]

#폰트를 정해줍니다
font_name = pg.font.match_font('arial')

#문자를 그려주는 함수입니다
def draw_text(surf, text, font_size, x, y):
    font = pg.font.Font(font_name, font_size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)
    
#적용했을시의 모습입니다
#게임 오버 스크린을 출력합니다
#아무 키나 눌렀을 시 메인화면으로 돌아갑니다
def game_over(value, is_multi=False):
    font1 = pg.font.SysFont("arial", 64, True, False)
    font2 = pg.font.SysFont("arial", 32, True, False)
    txt_surface1 = font1.render("Game Over", True, colors[1])
    if not is_multi:
        txt_surface2 = font2.render("deleted line : " + str(value), True, colors[5])
    else:
        if value == 3:
            txt_surface2 = font1.render("Computer Win!", True, colors[5])
        else:
            txt_surface2 = font1.render("Player" + str(value) + " Win", True, colors[5])
    txt_surface3 = font2.render("Press Enter key to return", True, colors[4])
    screen.blit(txt_surface1, (size[0] / 2 - txt_surface1.get_width() / 2, size[1] / 4))
    screen.blit(txt_surface2, (size[0] / 2 - txt_surface2.get_width() / 2, size[1] * 3 / 8))
    screen.blit(txt_surface3, (size[0] / 2 - txt_surface3.get_width() / 2, size[1] / 2))
    pg.display.flip()

    run = True
    while run:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_SPACE or event.key == pg.K_RETURN:
                    run = False
