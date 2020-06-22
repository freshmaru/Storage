#프로그램명 : score
#작성자 : 오기탁
#조명 : 하이파이
#라인 삭제를 통해 점수를 구현하는 함수입니다
#아래 함수들을 기반으로 프로젝트에 적용하였습니다


score = 0

self.line_score += self.attack_stack

 def get_score(self):
     return self.game.line_score

#화면에 문자를 출력하는 함수
def draw_text(surf, text, font_size, x, y):
    font = pg.font.Font(font_name, font_size)
    text_surface = font.render(text, True, WHITE)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    surf.blit(text_surface, text_rect)

#문자 출력
def draw_score(surf, grid, score=0, last_score=0):
    # current score
    draw_text(screen, "Score: " + str(score), 22, size[0], size[1])

    # last score
    draw_text(screen, 'High Score: ' + str(last_score), 1, 255, 255)

#지금까지의 기록을 유지하는 함수
# scores.txt파일에 0을 채워 넣은 후 저장하여 사용한다
def update_score(nscore):
    score = max_score()

    with open('scores.txt', 'w') as f:
        if int(score) > nscore:
            f.write(str(score))
        else:
            f.write(str(nscore))

#기록된 점수를 출력한다
def max_score():
    with open('scores.txt', 'r') as f:
        lines = f.readlines()
        score = lines[0].strip()

    return score
