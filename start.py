#프로그램명 : multi_play
#작성자 : 오기탁
#조명 : 하이파이
#start파일에 포함되는 로컬 플레이 함수
#객체 두 개를 가지고 게임을 플레이하는 함수입니다

def multi_play():
    run = True
    key_set1 = {'right': pg.K_RIGHT, 'left': pg.K_LEFT, 'up': pg.K_UP, 'down': pg.K_DOWN, 'drop': pg.K_RETURN}
    key_set2 = {'right': pg.K_d, 'left': pg.K_a, 'up': pg.K_w, 'down': pg.K_s, 'drop': pg.K_SPACE}
    player1 = Player('left', key_set1)
    player2 = Player('right', key_set2)
    Player.make_multi(player1, player2)
    screen.fill(WHITE)
    while run:
        for event in pg.event.get():
            if event.type == pg.QUIT:
                run = False
                pg.display.quit()
                quit()
            player1.key_input(event)
            player2.key_input(event)

        player1.move_piece()        #board에서 블럭을 움직이고 탐지한다
        player2.move_piece()
        player1.fall_time_check()
        player2.fall_time_check()
        player1.draw_board(screen)
        player2.draw_board(screen)
        clock.tick(FPS)
        pg.display.flip()
        if player1.is_game_over() or player2.is_game_over():
            run = False
            print("게임 오버 구현하기")


