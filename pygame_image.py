import sys
import pygame as pg


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("ex01/fig/pg_bg.jpg")
    bg_img1 =pg.transform.flip(bg_img,True,False)
    tori_img = pg.image.load("ex01/fig/3.png")
    tori_img =pg.transform.flip(tori_img,True,False)
    tori_img1=pg.transform.rotozoom(tori_img,10,1.0)
    tori_imgs = [tori_img,tori_img1]
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return
        a=(tmr%2400)
        b=tmr%200
        screen.blit(bg_img, [-a, 0])
        screen.blit(bg_img1, [1600-a, 0])
        if b>100:
             screen.blit(tori_imgs[0],[300,200])
        else:
            screen.blit(tori_imgs[1],[300,200])
        pg.display.update()
        tmr += 1     
        clock.tick(100)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()