import pygame as pg, sys, random
pg.init();

win_text="WINS: 0"
lose_text="LOSE: 0"
round_ended=False
main_color=(255,255,255)
wins_count=0
lose_count=0
mouse_pos_snap=(0,0)

grid=[]
for i in range(3):
    grid.append([0,0,0])

fnt=pg.font.SysFont('timesnewroman',  15)
screen=pg.display.set_mode((64*3,64*4))

def main():
    while True:
        screen.fill((80,80,80))
        win_text="WINS: %s" % wins_count
        lose_text="LOSE: %s" % lose_count

        for ev in pg.event.get():
            if ev.type == pg.QUIT:
                pg.quit() # quit the screen
                sys.exit()

            if ev.type == pg.KEYDOWN:
                if ev.key == pg.K_r:
                    reset_grid()

            if ev.type == pg.MOUSEBUTTONDOWN:
                on_click(mouse_pos_snap)

        for xx in range(3):
            for yy in range(3):
                pg.draw.rect(screen, (160,160,160), (xx*64,yy*64,64,64))

        for yy in range(3):
            for xx in range(3):
                o_pos=(xx*64,yy*64)
                pos=(o_pos[0]+32,o_pos[1]+32)
                match grid[yy][xx]:
                    case 1:
                        pg.draw.line(screen, main_color, (pos[0]-16,pos[1]-16), (pos[0]+16,pos[1]+16), 2)
                        pg.draw.line(screen, main_color, (pos[0]+16,pos[1]-16), (pos[0]-16,pos[1]+16), 2)

                    case 2:
                        pg.draw.circle(screen, main_color, pos, 32.0, 2)

                    case _:
                        pass

        mouse_pos=pg.mouse.get_pos()
        mouse_pos_snap=(int(mouse_pos[0]/64),int(mouse_pos[1]/64))
        pg.draw.rect(screen, (200,200,200), (mouse_pos_snap[0]*64,mouse_pos_snap[1]*64,64,64), 2)

        screen.blit(fnt.render(win_text,False, (0,0,0)), (8+1,(32*6.4)+1))
        screen.blit(fnt.render(win_text,False, (255,255,255)), (8,32*6.4))
        
        screen.blit(fnt.render(lose_text,False, (0,0,0)), (8+1,(32*6.4)+16+1))
        screen.blit(fnt.render(lose_text,False, (255,255,255)), (8,(32*6.4)+16))
       
        pg.display.flip()


def on_click(coord):
    global round_ended, main_color
    if coord[1]>2 | round_ended==True:
        return 0

    gval=grid[coord[1]][coord[0]]
    if gval==0:
        grid[coord[1]][coord[0]]=1;
        pg.time.delay(5);

        if check_player_win(1):
            global wins_count
            wins_count=wins_count+1;
            round_ended=True;
            main_color=(127,255,0)
            return 0;

        pg.time.delay(5);
        on_bot_click();
        pg.time.delay(5);

        if check_player_win(2):
            global lose_count
            lose_count=lose_count+1; 
            round_ended=True;
            main_color=(220,20,60)
            return 0;


def check_player_win(val):
    if grid[0][0]==val & grid[1][0]==val & grid[2][0]==val:
        return True

    if grid[0][1]==val & grid[1][1]==val & grid[2][1]==val:
        return True

    if grid[0][2]==val & grid[1][2]==val & grid[2][2]==val:
        return True

    if grid[0][0]==val & grid[0][1]==val & grid[0][2]==val:
        return True

    if grid[1][0]==val & grid[1][1]==val & grid[1][2]==val:
        return True

    if grid[2][0]==val & grid[2][1]==val & grid[2][2]==val:
        return True

    if grid[0][0]==val & grid[1][1]==val & grid[2][2]==val:
         return True 

    if grid[2][0]==val & grid[1][1]==val & grid[0][2]==val:
         return True 

    return False

def on_bot_click():
    has_space=False;
    for y in range(3):
        for x in range(3):
            if grid[y][x]==0:
                has_space=True
                break;

    if has_space:
        x=random.randint(0,2)
        y=random.randint(0,2)
        while grid[y][x]!=0:
            x=random.randint(0,2)
            y=random.randint(0,2)
        grid[y][x]=2;


def reset_grid():
    global grid, round_ended, main_color
    round_ended=False;
    grid=[[0,0,0],[0,0,0],[0,0,0]]
    main_color=(255,255,255)

main();