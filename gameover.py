#프로그램명 : game_over
#작성자 : 오기탁
#조명 : 하이파이
#게임 오버를 구현하는 함수입니다
#텍스트를 출력하고 메인으로 돌아가거나 게임을 재시작합니다.

BLACK = (0, 0, 0)

font_name = pg.font.match_font('arial')

#문자를 그려주는 함수입니다
def draw_text(surf, text, font_size, x, y):
    font = pg.font.Font(font_name, font_size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#게임 오버 스크린을 출력합니다
#스페이스바를 눌렀을 시 메인화면으로 돌아갑니다
#아무 키나 눌렀을시 게임을 다시 시작합니다
def show_go_screen():
    draw_text(screen, "Game Over", 64, size[0] / 2, size[1] / 4)
    draw_text(screen, "Press space to return", 22, size[0] / 2, size[1] / 2)
    draw_text(screen, "Press a key to begin", 18, size[0] / 2, size[1] * 3 / 4)
    pg.display.flip()
    while waiting:
        clock.tick(FPS)
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.KEYUP:
                waiting = False
