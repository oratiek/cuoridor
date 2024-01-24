import pyxel



class Quoridor :
    def __init__(self) :
        pyxel.init(349, 359 , fps=60)
        self.player1_x = 0 #プレイヤー1のx座標(0-8で変動)
        self.player1_y = 4 #プレイヤー1のx座標(0-8で変動)
        self.player2_x = 8 #プレイヤー1のx座標(0-8で変動)
        self.player2_y = 4 #プレイヤー1のx座標(0-8で変動)

        self.player1_vector = 0 #1:上 2:右 3:下 4:左
        self.player1_vector_dia = 0 #1:反時計側 2:時計側
        self.player2_vector = 0 #1:上 2:右 3:下 4:左
        self.player2_vector_dia = 0 #1:反時計側 2:時計側

        self.arrow_color = 0 #矢印の色
        self.arrow_color_player1 = 5 #プレイヤー1の矢印の色
        self.arrow_color_player2 = 8 #プレイヤー2の矢印の色
        self.arrow_color_cant = 13 #不可能時の矢印の色

        self.player_now = pyxel.rndi(1,2) #現在のプレイヤー
        self.player_before = self.player_now #1f前のプレイヤー

        self.install_mode = 0 #0:移動モード 1:縦壁配置 2:横壁配置
        self.wall_x = 1 #設置予定壁のx座標(1-8で変動)
        self.wall_y = 1 #設置予定壁のy座標(1-8で変動)

        self.wallnum_player1 = 10 #プレイヤー1の壁の所持数
        self.wallnum_player2 = 10 #プレイヤー2の壁の所持数

        self.gamemode = 0 #0:ゲームプレイ画面 1:ゲーム終了

        self.turn_count = 1 #現在のターン数(100ターンで一周)
        self.first_judge = True #先攻プレイヤーならTrue、後攻プレイヤーならFalse
        self.player1_time = 0 #プレイヤー1の経過時間(単位:f、100分=6000秒=360000fで一周)
        self.player2_time = 0 #プレイヤー2の経過時間(単位:f、100分=6000秒=360000fで一周)


        #self.wall_make_can = False #wall_can関数の戻り値として使う変数
        self.wall_make_can_player1 = False #wall_can関数の戻り値に利用する変数
        self.wall_make_can_player2 = False #wall_can関数の戻り値に利用する変数

        self.search_algorithm = True #探索アルゴリズムのレベル True:High False:low
        
        #1:縦 2:横
        self.wall_list = [[2,2,2,2,2,2,2,2,2,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,2,2,2,2,2,2,2,2,2]
                          ]
        
        self.wall_list_tent = [[2,2,2,2,2,2,2,2,2,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,0,0,0,0,0,0,0,0,1],
                          [1,2,2,2,2,2,2,2,2,2]
                          ]
        
        self.player1_can_move_list = [[0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player1_can_move_list_before = [[9,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player2_can_move_list = [[0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player2_can_move_list_before = [[9,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]

        pyxel.run(self.update, self.draw)

    
    def wall_can(self,y,x,dir,search_mode=True):
      if search_mode or self.search_algorithm:
        for xs in range(10):
            for ys in range(10):
                self.wall_list_tent[ys][xs] = self.wall_list[ys][xs]
        self.wall_list_tent[y][x] = dir
        self.wall_make_can_player1 = False
        self.wall_make_can_player2 = False

        self.player1_can_move_list = [[0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player1_can_move_list_before = [[9,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player2_can_move_list = [[0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player2_can_move_list_before = [[9,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0],
                                      [0,0,0,0,0,0,0,0,0]]
        
        self.player1_can_move_list[self.player1_y][self.player1_x] = 1
        self.player2_can_move_list[self.player2_y][self.player2_x] = 1

        while True:
            #self.player1_can_move_list_before = self.player1_can_move_list
            #self.player2_can_move_list_before = self.player2_can_move_list
            for xs in range (9):
                for ys in range(9):
                    self.player1_can_move_list_before[ys][xs] = self.player1_can_move_list[ys][xs]
                    self.player2_can_move_list_before[ys][xs] = self.player2_can_move_list[ys][xs]
            for xs in range(9):
                for ys in range(9):
                    if self.player1_can_move_list[ys][xs] == 1:
                        if ys > 0:
                            if not(self.wall_list_tent[ys][xs] == 2 or self.wall_list_tent[ys][xs+1] == 2):
                                self.player1_can_move_list[ys-1][xs] = 1
                        if xs < 8:
                            if not(self.wall_list_tent[ys][xs+1] == 1 or self.wall_list_tent[ys+1][xs+1] == 1):
                                self.player1_can_move_list[ys][xs+1] = 1
                        if ys < 8:
                            if not(self.wall_list_tent[ys+1][xs] == 2 or self.wall_list_tent[ys+1][xs+1] == 2):
                                self.player1_can_move_list[ys+1][xs] = 1
                        if xs > 0:
                            if not(self.wall_list_tent[ys][xs] == 1 or self.wall_list_tent[ys+1][xs] == 1):
                                self.player1_can_move_list[ys][xs-1] = 1
                    if self.player2_can_move_list[ys][xs] == 1:
                        if ys > 0:
                            if not(self.wall_list_tent[ys][xs] == 2 or self.wall_list_tent[ys][xs+1] == 2):
                                self.player2_can_move_list[ys-1][xs] = 1
                        if xs < 8:
                            if not(self.wall_list_tent[ys][xs+1] == 1 or self.wall_list_tent[ys+1][xs+1] == 1):
                                self.player2_can_move_list[ys][xs+1] = 1
                        if ys < 8:
                            if not(self.wall_list_tent[ys+1][xs] == 2 or self.wall_list_tent[ys+1][xs+1] == 2):
                                self.player2_can_move_list[ys+1][xs] = 1
                        if xs > 0:
                            if not(self.wall_list_tent[ys][xs] == 1 or self.wall_list_tent[ys+1][xs] == 1):
                                self.player2_can_move_list[ys][xs-1] = 1
            if self.player1_can_move_list == self.player1_can_move_list_before and self.player2_can_move_list == self.player2_can_move_list_before:
                break
            
        for ys in range(9):
            if self.player1_can_move_list_before[ys][8] == 1:
                self.wall_make_can_player1 = True
            if self.player2_can_move_list_before[ys][0] == 1:
                self.wall_make_can_player2 = True
        
        if self.wall_make_can_player1 and self.wall_make_can_player2:
            return True
        else:
            return False
      else:
          return True

        


    def update(self):


      if self.install_mode == 0 and self.gamemode == 0:
        if self.player_now == 1:
            if pyxel.btnp(pyxel.KEY_W): # WASDキーで方向指定
                self.player1_vector = 1
                self.player1_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_A):
                self.player1_vector = 4
                self.player1_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_S):
                self.player1_vector = 3
                self.player1_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_D):
                self.player1_vector = 2
                self.player1_vector_dia = 0


            #斜め方向を確定させる
            if self.player1_x == self.player2_x and self.player1_y - 1 == self.player2_y:
              if self.wall_list[self.player1_y-1][self.player1_x] == 2 or self.wall_list[self.player1_y-1][self.player1_x+1] == 2:
                if (pyxel.btnp(pyxel.KEY_W) and pyxel.btn(pyxel.KEY_A)) or (pyxel.btn(pyxel.KEY_W) and pyxel.btnp(pyxel.KEY_A)):
                    self.player1_vector_dia = 1
                    self.player1_vector = 1
                if (pyxel.btnp(pyxel.KEY_W) and pyxel.btn(pyxel.KEY_D)) or (pyxel.btn(pyxel.KEY_W) and pyxel.btnp(pyxel.KEY_D)):
                    self.player1_vector_dia = 2
                    self.player1_vector = 1

            if self.player1_x+1 == self.player2_x and self.player1_y == self.player2_y:
              if self.wall_list[self.player1_y][self.player1_x+2] == 1 or self.wall_list[self.player1_y+1][self.player1_x+2] == 1:
                if (pyxel.btnp(pyxel.KEY_W) and pyxel.btn(pyxel.KEY_D)) or (pyxel.btn(pyxel.KEY_W) and pyxel.btnp(pyxel.KEY_D)):
                    self.player1_vector_dia = 1
                    self.player1_vector = 2
                if (pyxel.btnp(pyxel.KEY_D) and pyxel.btn(pyxel.KEY_S)) or (pyxel.btn(pyxel.KEY_D) and pyxel.btnp(pyxel.KEY_S)):
                    self.player1_vector_dia = 2
                    self.player1_vector = 2

            if self.player1_x == self.player2_x and self.player1_y + 1 == self.player2_y:
              if self.wall_list[self.player1_y+2][self.player1_x] == 2 or self.wall_list[self.player1_y+2][self.player1_x+1] == 2:
                if (pyxel.btnp(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_D)) or (pyxel.btn(pyxel.KEY_S) and pyxel.btnp(pyxel.KEY_D)):
                    self.player1_vector_dia = 1
                    self.player1_vector = 3
                if (pyxel.btnp(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_A)) or (pyxel.btn(pyxel.KEY_S) and pyxel.btnp(pyxel.KEY_A)):
                    self.player1_vector_dia = 2
                    self.player1_vector = 3

            if self.player1_x-1 == self.player2_x and self.player1_y == self.player2_y:
              if self.wall_list[self.player1_y][self.player1_x-1] == 1 or self.wall_list[self.player1_y+1][self.player1_x-1] == 1:
                if (pyxel.btnp(pyxel.KEY_S) and pyxel.btn(pyxel.KEY_A)) or (pyxel.btn(pyxel.KEY_S) and pyxel.btnp(pyxel.KEY_A)):
                    self.player1_vector_dia = 1
                    self.player1_vector = 4
                if (pyxel.btnp(pyxel.KEY_W) and pyxel.btn(pyxel.KEY_A)) or (pyxel.btn(pyxel.KEY_W) and pyxel.btnp(pyxel.KEY_A)):
                    self.player1_vector_dia = 2
                    self.player1_vector = 4
            
            
            #2024/1/2 25:33 ロブの結婚式が行われました。

            #移動
            if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player1_vector == 1: #and self.player1_y >= 1:
                if self.player1_x == self.player2_x and self.player1_y - 1 == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y-1][self.player1_x] == 2) and (not self.wall_list[self.player1_y-1][self.player1_x+1] == 2):
                        self.player1_y -= 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y-1][self.player1_x] == 1 or self.wall_list[self.player1_y][self.player1_x] == 1)):
                        self.player1_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y -= 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y-1][self.player1_x+1] == 1 or self.wall_list[self.player1_y][self.player1_x+1] == 1)):
                        self.player1_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y -= 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                elif not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2):
                    self.player1_y -= 1 #プレイヤー飛び越えを行わない
                    self.player_now = 2
                    self.player1_vector = 0
                    self.player1_vector_dia = 0

                

            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player1_vector == 2: #and self.player1_y >= 1:
                if self.player1_x+1 == self.player2_x and self.player1_y == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x+2] == 1 or self.wall_list[self.player1_y+1][self.player1_x+2] == 1):
                        self.player1_x += 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y][self.player1_x+1] == 2 or self.wall_list[self.player1_y][self.player1_x+2] == 2)):
                        self.player1_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y -= 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y+1][self.player1_x+1] == 2 or self.wall_list[self.player1_y+1][self.player1_x+2] == 2)):
                        self.player1_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y += 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                elif not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1):
                    self.player1_x += 1 #プレイヤー飛び越えを行わない
                    self.player_now = 2
                    self.player1_vector = 0
                    self.player1_vector_dia = 0
            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player1_vector == 3: #and self.player1_y >= 1:
                if self.player1_x == self.player2_x and self.player1_y + 1 == self.player2_y and(not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y+2][self.player1_x] == 2) and (not self.wall_list[self.player1_y+2][self.player1_x+1] == 2):
                        self.player1_y += 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y+1][self.player1_x+1] == 1 or self.wall_list[self.player1_y+2][self.player1_x+1] == 1)):
                        self.player1_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y += 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y+1][self.player1_x] == 1 or self.wall_list[self.player1_y+2][self.player1_x] == 1)):
                        self.player1_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y += 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                elif not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2):
                    self.player1_y += 1 #プレイヤー飛び越えを行わない
                    self.player_now = 2
                    self.player1_vector = 0
                    self.player1_vector_dia = 0
            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player1_vector == 4: #and self.player1_y >= 1:
                if self.player1_x-1 == self.player2_x and self.player1_y == self.player2_y and(not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x-1] == 1 or self.wall_list[self.player1_y+1][self.player1_x-1] == 1):
                        self.player1_x -= 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x-1] == 2)):
                        self.player1_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y += 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x-1] == 2)):
                        self.player1_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player1_y -= 1
                        self.player_now = 2
                        self.player1_vector = 0
                        self.player1_vector_dia = 0
                elif not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1):
                    self.player1_x -= 1 #プレイヤー飛び越えを行わない
                    self.player_now = 2
                    self.player1_vector = 0
                    self.player1_vector_dia = 0

                
        elif self.player_now == 2:
            if pyxel.btnp(pyxel.KEY_UP): # 矢印キーで方向指定
                self.player2_vector = 1
                self.player2_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_LEFT):
                self.player2_vector = 4
                self.player2_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_DOWN):
                self.player2_vector = 3
                self.player2_vector_dia = 0
            if pyxel.btnp(pyxel.KEY_RIGHT):
                self.player2_vector = 2
                self.player2_vector_dia = 0


            #斜め方向を確定させる
            if self.player2_x == self.player1_x and self.player2_y - 1 == self.player1_y:
              if self.wall_list[self.player2_y-1][self.player2_x] == 2 or self.wall_list[self.player2_y-1][self.player2_x+1] == 2:
                if (pyxel.btnp(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_UP) and pyxel.btnp(pyxel.KEY_LEFT)):
                    self.player2_vector_dia = 1
                    self.player2_vector = 1
                if (pyxel.btnp(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_RIGHT)) or (pyxel.btn(pyxel.KEY_UP) and pyxel.btnp(pyxel.KEY_RIGHT)):
                    self.player2_vector_dia = 2
                    self.player2_vector = 1

            if self.player2_x+1 == self.player1_x and self.player2_y == self.player1_y:
              if self.wall_list[self.player2_y][self.player2_x+2] == 1 or self.wall_list[self.player2_y+1][self.player2_x+2] == 1:
                if (pyxel.btnp(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_RIGHT)) or (pyxel.btn(pyxel.KEY_UP) and pyxel.btnp(pyxel.KEY_RIGHT)):
                    self.player2_vector_dia = 1
                    self.player2_vector = 2
                if (pyxel.btnp(pyxel.KEY_RIGHT) and pyxel.btn(pyxel.KEY_DOWN)) or (pyxel.btn(pyxel.KEY_RIGHT) and pyxel.btnp(pyxel.KEY_DOWN)):
                    self.player2_vector_dia = 2
                    self.player2_vector = 2

            if self.player2_x == self.player1_x and self.player2_y + 1 == self.player1_y:
              if self.wall_list[self.player2_y+2][self.player2_x] == 2 or self.wall_list[self.player2_y+2][self.player2_x+1] == 2:
                if (pyxel.btnp(pyxel.KEY_DOWN) and pyxel.btn(pyxel.KEY_RIGHT)) or (pyxel.btn(pyxel.KEY_DOWN) and pyxel.btnp(pyxel.KEY_RIGHT)):
                    self.player2_vector_dia = 1
                    self.player2_vector = 3
                if (pyxel.btnp(pyxel.KEY_DOWN) and pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_DOWN) and pyxel.btnp(pyxel.KEY_LEFT)):
                    self.player2_vector_dia = 2
                    self.player2_vector = 32

            if self.player2_x-1 == self.player1_x and self.player2_y == self.player1_y:
              if self.wall_list[self.player2_y][self.player2_x-1] == 1 or self.wall_list[self.player2_y+1][self.player2_x-1] == 1:
                if (pyxel.btnp(pyxel.KEY_DOWN) and pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_DOWN) and pyxel.btnp(pyxel.KEY_LEFT)):
                    self.player2_vector_dia = 1
                    self.player2_vector = 4
                if (pyxel.btnp(pyxel.KEY_UP) and pyxel.btn(pyxel.KEY_LEFT)) or (pyxel.btn(pyxel.KEY_UP) and pyxel.btnp(pyxel.KEY_LEFT)):
                    self.player2_vector_dia = 2
                    self.player2_vector = 4

            #移動
            if (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player2_vector == 1: #and self.player1_y >= 1:
                if self.player2_x == self.player1_x and self.player2_y - 1 == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y-1][self.player2_x] == 2) and (not self.wall_list[self.player2_y-1][self.player2_x+1] == 2):
                        self.player2_y -= 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y-1][self.player2_x] == 1 or self.wall_list[self.player2_y][self.player2_x] == 1)):
                        self.player2_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y -= 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y-1][self.player2_x+1] == 1 or self.wall_list[self.player2_y][self.player2_x+1] == 1)):
                        self.player2_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y -= 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                elif not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2):
                    self.player2_y -= 1 #プレイヤー飛び越えを行わない
                    self.player_now = 1
                    self.player2_vector = 0
                    self.player2_vector_dia = 0

                

            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player2_vector == 2: #and self.player2_y >= 1:
                if self.player2_x+1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x+2] == 1 or self.wall_list[self.player2_y+1][self.player2_x+2] == 1):
                        self.player2_x += 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y][self.player2_x+1] == 2 or self.wall_list[self.player2_y][self.player2_x+2] == 2)):
                        self.player2_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y -= 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y+1][self.player2_x+1] == 2 or self.wall_list[self.player2_y+1][self.player2_x+2] == 2)):
                        self.player2_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y += 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                elif not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1):
                    self.player2_x += 1 #プレイヤー飛び越えを行わない
                    self.player_now = 1
                    self.player2_vector = 0
                    self.player2_vector_dia = 0
            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player2_vector == 3: #and self.player2_y >= 1:
                if self.player2_x == self.player1_x and self.player2_y + 1 == self.player1_y and (not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y+2][self.player2_x] == 2) and (not self.wall_list[self.player2_y+2][self.player2_x+1] == 2):
                        self.player2_y += 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y+1][self.player2_x+1] == 1 or self.wall_list[self.player2_y+2][self.player2_x+1] == 1)):
                        self.player2_x += 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y += 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y+1][self.player2_x] == 1 or self.wall_list[self.player2_y+2][self.player2_x] == 1)):
                        self.player2_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y += 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                elif not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2):
                    self.player2_y += 1 #プレイヤー飛び越えを行わない
                    self.player_now = 1
                    self.player2_vector = 0
                    self.player2_vector_dia = 0
            elif (pyxel.btnp(pyxel.KEY_SPACE) or pyxel.btnp(pyxel.KEY_RETURN))  and self.player2_vector == 4: #and self.player2_y >= 1:
                if self.player2_x-1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x-1] == 1 or self.wall_list[self.player2_y+1][self.player2_x-1] == 1):
                        self.player2_x -= 2 #プレイヤー飛び越えを行う、壁なし
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x-1] == 2)):
                        self.player2_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y += 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x-1] == 2)):
                        self.player2_x -= 1 #プレイヤー飛び越えを行う、壁あり
                        self.player2_y -= 1
                        self.player_now = 1
                        self.player2_vector = 0
                        self.player2_vector_dia = 0
                elif not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1):
                    self.player2_x -= 1 #プレイヤー飛び越えを行わない
                    self.player_now = 1
                    self.player2_vector = 0
                    self.player2_vector_dia = 0

    
      if (self.install_mode == 1 or self.install_mode == 2) and self.gamemode == 0:
          if self.player_now == 1:
              if pyxel.btnp(pyxel.KEY_W):
                  self.wall_y -= 1
              if pyxel.btnp(pyxel.KEY_D):
                  self.wall_x += 1
              if pyxel.btnp(pyxel.KEY_S):
                  self.wall_y += 1
              if pyxel.btnp(pyxel.KEY_A):
                  self.wall_x -= 1
          elif self.player_now == 2:
              if pyxel.btnp(pyxel.KEY_UP):
                  self.wall_y -= 1
              if pyxel.btnp(pyxel.KEY_RIGHT):
                  self.wall_x += 1
              if pyxel.btnp(pyxel.KEY_DOWN):
                  self.wall_y += 1
              if pyxel.btnp(pyxel.KEY_LEFT):
                  self.wall_x -= 1 

          if self.wall_x >= 9:
              self.wall_x = 8
          elif self.wall_x <= 0:        
              self.wall_x = 1
          if self.wall_y >= 9:
              self.wall_y = 8
          elif self.wall_y <= 0:        
              self.wall_y = 1
        
      if self.install_mode == 1 and (pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE)) and self.gamemode == 0:
          if self.wall_list[self.wall_y][self.wall_x] == 0 and (not(self.wall_list[self.wall_y-1][self.wall_x] == 1 or self.wall_list[self.wall_y+1][self.wall_x] == 1)) and self.wall_can(self.wall_y,self.wall_x,self.install_mode):
              self.wall_list[self.wall_y][self.wall_x] = 1
              if self.player_now == 1:
                  self.player_now = 2
                  self.wallnum_player1 -= 1
              else:
                  self.player_now = 1
                  self.wallnum_player2 -= 1
      elif self.install_mode == 2 and (pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE)) and self.gamemode == 0:
          if self.wall_list[self.wall_y][self.wall_x] == 0 and (not(self.wall_list[self.wall_y][self.wall_x-1] == 2 or self.wall_list[self.wall_y][self.wall_x+1] == 2)) and self.wall_can(self.wall_y,self.wall_x,self.install_mode):
              self.wall_list[self.wall_y][self.wall_x] = 2
              if self.player_now == 1:
                  self.player_now = 2
                  self.wallnum_player1 -= 1
              else:
                  self.player_now = 1
                  self.wallnum_player2 -= 1
              


        
      if self.player_now == self.player_before:
            if pyxel.btnp(pyxel.KEY_SHIFT) and ((self.player_now == 1 and self.wallnum_player1 >= 1) or (self.player_now == 2 and self.wallnum_player2 >= 1)):
                self.install_mode += 1
                self.player1_vector = 0 #1:上 2:右 3:下 4:左
                self.player1_vector_dia = 0 #1:反時計側 2:時計側
                self.player2_vector = 0 #1:上 2:右 3:下 4:左
                self.player2_vector_dia = 0 #1:反時計側 2:時計側
                if self.install_mode >= 3:
                    self.install_mode = 0
                #if self.install_mode == 1:
                    #for y in range(8):
                        #for x in range(8):
                            #if self.wall_list[8-y][8-x] == 0 and (not(self.wall_list[7-y][8-x] == 1 or self.wall_list[9-y][8-x] == 1)):
                                #self.wall_x = 8-x
                                #self.wall_y = 8-y
                #if self.install_mode == 2:
                    #for y in range(8):
                        #for x in range(8):
                            #if self.wall_list[8-y][8-x] == 0 and (not(self.wall_list[8-y][7-x] == 2 or self.wall_list[8-y][9-x] == 2)):
                                #self.wall_x = 8-x
                                #self.wall_y = 8-y

      else:
            self.install_mode = 0
            self.player1_vector = 0 #1:上 2:右 3:下 4:左
            self.player1_vector_dia = 0 #1:反時計側 2:時計側
            self.player2_vector = 0 #1:上 2:右 3:下 4:左
            self.player2_vector_dia = 0 #1:反時計側 2:時計側

            if self.player1_x < 8 and self.player2_x > 0:

                if self.first_judge:
                    self.first_judge = False
                else:
                    self.first_judge = True
                    self.turn_count += 1
                    if self.turn_count >= 100:
                        self.turn_count -= 100

        
      


      if self.gamemode == 0:
          if self.player_now == 1:
              self.player1_time += 1
              if self.player1_time >= 360000:
                  self.player1_time -= 360000
          elif self.player_now == 2:
              self.player2_time += 1
              if self.player2_time >= 360000:
                  self.player2_time -= 360000


          if self.player1_x == 8:
              self.gamemode = 1
              self.player_now = 1
          elif self.player2_x == 0:
              self.gamemode = 1
              self.player_now = 2
      elif self.gamemode == 1:
          if pyxel.mouse_x >= 160 and pyxel.mouse_x <= 250 :
              if pyxel.mouse_y >= 160 and pyxel.mouse_y <= 250 :
                  if pyxel.btnp(pyxel.MOUSE_BUTTON_LEFT):
                      self.gamemode = 0
                      self.player1_x = 0 #プレイヤー1のx座標(0-8で変動)
                      self.player1_y = 4 #プレイヤー1のx座標(0-8で変動)
                      self.player2_x = 8 #プレイヤー1のx座標(0-8で変動)
                      self.player2_y = 4 #プレイヤー1のx座標(0-8で変動)

                      self.player1_vector = 0 #1:上 2:右 3:下 4:左
                      self.player1_vector_dia = 0 #1:反時計側 2:時計側
                      self.player2_vector = 0 #1:上 2:右 3:下 4:左
                      self.player2_vector_dia = 0 #1:反時計側 2:時計側

                      self.arrow_color = 0 #矢印の色
                      self.arrow_color_player1 = 5 #プレイヤー1の矢印の色
                      self.arrow_color_player2 = 8 #プレイヤー2の矢印の色
                      self.arrow_color_cant = 13 #不可能時の矢印の色
                      pyxel.mouse(False)
                      self.player_before = self.player_now #1f前のプレイヤー

                      self.install_mode = 0 #0:移動モード 1:縦壁配置 2:横壁配置
                      self.wall_x = 1 #設置予定壁のx座標(1-8で変動)
                      self.wall_y = 1 #設置予定壁のy座標(1-8で変動)

                      self.wallnum_player1 = 10 #プレイヤー1の壁の所持数
                      self.wallnum_player2 = 10 #プレイヤー2の壁の所持数

                      self.turn_count = 1 #現在のターン数(100ターンで一周)
                      self.first_judge = True #先攻プレイヤーならTrue、後攻プレイヤーならFalse
                      self.player1_time = 0 #プレイヤー1の経過時間(単位:f、100分=6000秒=360000fで一周)
                      self.player2_time = 0 #プレイヤー2の経過時間(単位:f、100分=6000秒=360000fで一周)
            
                       #1:縦 2:横
                      self.wall_list = [[2,2,2,2,2,2,2,2,2,1],
                                      [1,0,0,0,0,0,0,0,0,1],
                                      [1,0,0,0,0,0,0,0,0,1],
                                      [1,0,0,0,0,0,0,0,0,1],
                                      [1,0,0,0,0,0,0,0,0,1],
                                      [1,0,0,0,0,0,0,0,0,1],
                                      [1,0,0,0,0,0,0,0,0,1],
                                      [1,0,0,0,0,0,0,0,0,1],
                                      [1,0,0,0,0,0,0,0,0,1],
                                      [1,2,2,2,2,2,2,2,2,2]
                                      ]
                      
          if pyxel.btnp(pyxel.KEY_RETURN) or pyxel.btnp(pyxel.KEY_SPACE) :
              self.gamemode = 0
              self.player1_x = 0 #プレイヤー1のx座標(0-8で変動)
              self.player1_y = 4 #プレイヤー1のx座標(0-8で変動)
              self.player2_x = 8 #プレイヤー1のx座標(0-8で変動)
              self.player2_y = 4 #プレイヤー1のx座標(0-8で変動)

              self.player1_vector = 0 #1:上 2:右 3:下 4:左
              self.player1_vector_dia = 0 #1:反時計側 2:時計側
              self.player2_vector = 0 #1:上 2:右 3:下 4:左
              self.player2_vector_dia = 0 #1:反時計側 2:時計側

              self.arrow_color = 0 #矢印の色
              self.arrow_color_player1 = 5 #プレイヤー1の矢印の色
              self.arrow_color_player2 = 8 #プレイヤー2の矢印の色
              self.arrow_color_cant = 13 #不可能時の矢印の色

              self.player_before = self.player_now #1f前のプレイヤー

              self.install_mode = 0 #0:移動モード 1:縦壁配置 2:横壁配置
              self.wall_x = 1 #設置予定壁のx座標(1-8で変動)
              self.wall_y = 1 #設置予定壁のy座標(1-8で変動)

              self.wallnum_player1 = 10 #プレイヤー1の壁の所持数
              self.wallnum_player2 = 10 #プレイヤー2の壁の所持数

              self.turn_count = 1 #現在のターン数(100ターンで一周)
              self.first_judge = True #先攻プレイヤーならTrue、後攻プレイヤーならFalse
              self.player1_time = 0 #プレイヤー1の経過時間(単位:f、100分=6000秒=360000fで一周)
              self.player2_time = 0 #プレイヤー2の経過時間(単位:f、100分=6000秒=360000fで一周)
            
              #1:縦 2:横
              self.wall_list = [[2,2,2,2,2,2,2,2,2,1],
                              [1,0,0,0,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,1],
                              [1,0,0,0,0,0,0,0,0,1],
                              [1,2,2,2,2,2,2,2,2,2]
                              ]

              



      self.player_before = self.player_now




        

    #矢印マークの上にバツマークを描画する     
    def cross__arrow_draw(self,x,y):
        if self.arrow_color == self.arrow_color_cant:
            pyxel.tri(x-7,y-9,x-9,y-7,x+9,y+7,8)
            pyxel.tri(x+7,y+9,x-9,y-7,x+9,y+7,8)

            pyxel.tri(x+7,y-9,x+9,y-7,x-9,y+7,8)
            pyxel.tri(x-7,y+9,x+9,y-7,x-9,y+7,8)

    def cross__wall_draw(self,x,y):
        #if self.arrow_color == self.arrow_color_cant:
            pyxel.tri(x-7,y-9,x-9,y-7,x+9,y+7,8)
            pyxel.tri(x+7,y+9,x-9,y-7,x+9,y+7,8)

            pyxel.tri(x+7,y-9,x+9,y-7,x-9,y+7,8)
            pyxel.tri(x-7,y+9,x+9,y-7,x-9,y+7,8)

    def box_color(self,x,y):
      if self.install_mode == 0 and self.gamemode == 0:
        pyxel.rectb(7 + x * 38, 7 + y * 38 ,31,31,11)
        if self.player_now == 1:
            pyxel.rectb(8 + x * 38, 8 + y * 38 ,29,29,12)
        elif self.player_now == 2:
            pyxel.rectb(8 + x * 38, 8 + y * 38 ,29,29,14)
        

    
    def draw(self) :
        pyxel.cls(7)


        if self.player_now == 1:
            pyxel.rectb(0,0,349,359,12)
            pyxel.rectb(1,1,347,357,12)
        elif self.player_now == 2:
            pyxel.rectb(0,0,349,359,14)
            pyxel.rectb(1,1,347,357,14)
   
        for x in range(9):
            for y in range(9):
                if self.gamemode == 0:
                    pyxel.rectb(7 + x * 38, 7 + y * 38 ,31,31,0) #マス目表示
                elif self.player_now == 1:
                    pyxel.rectb(7 + x * 38, 7 + y * 38 ,31,31,12) #マス目表示
                elif self.player_now == 2:
                    pyxel.rectb(7 + x * 38, 7 + y * 38 ,31,31,14) #マス目表示
        pyxel.rect(7 + self.player1_x * 38, 7 + self.player1_y * 38 ,31,31,12)
        pyxel.rect(7 + self.player2_x * 38, 7 + self.player2_y * 38 ,31,31,14)
        pyxel.rect(7,344,11,11,12)
        pyxel.text(18,347," x "+str(self.wallnum_player1),12)
        pyxel.rect(311,344,11,11,14)
        pyxel.text(322,347," x "+str(self.wallnum_player2),14)
        pyxel.text(162,347,"TURN "+str(self.turn_count),0)
        if self.player_now == 1:
            pyxel.text(132,347,str(self.player1_time // 3600).zfill(2)+":"+str((self.player1_time % 3600)//60).zfill(2),12)
            pyxel.text(199,347,str(self.player2_time // 3600).zfill(2)+":"+str((self.player2_time % 3600)//60).zfill(2),0)
        elif self.player_now == 2:
            pyxel.text(132,347,str(self.player1_time // 3600).zfill(2)+":"+str((self.player1_time % 3600)//60).zfill(2),0)
            pyxel.text(199,347,str(self.player2_time // 3600).zfill(2)+":"+str((self.player2_time % 3600)//60).zfill(2),14)

        if self.gamemode == 0:
            if self.player_now == 1:
                pyxel.text(45,347,"Player1 TURN",12)
            if self.player_now == 2:
                pyxel.text(257,347,"Player2 TURN",14)
        elif self.gamemode == 1:
            pyxel.mouse(True)
            if self.player_now == 1:
                pyxel.text(175,175,"Player1 WIN!",12)
                pyxel.text(175,183,"Click Here to Retry",12)
                pyxel.text(249,347,"Enter to Retry",0) #restartと迷ったけど勝った側は二度とやりたくないだろうから敗者のretry
            if self.player_now == 2:
                pyxel.text(175,175,"Player2 WIN!",14)
                pyxel.text(175,183,"Click Here to Retry",14)
                pyxel.text(45,347,"Enter to Retry",0)
        
        

        if self.player_now == 1:

            #マスのカラー変更-上
            if self.player1_x == self.player2_x and self.player1_y - 1 == self.player2_y and(not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y-1][self.player1_x] == 2) and (not self.wall_list[self.player1_y-1][self.player1_x+1] == 2):
                        self.box_color(self.player1_x,self.player1_y-2) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player1_y-1][self.player1_x] == 1 or self.wall_list[self.player1_y][self.player1_x] == 1):
                            self.box_color(self.player1_x-1,self.player1_y-1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player1_y-1][self.player1_x+1] == 1 or self.wall_list[self.player1_y][self.player1_x+1] == 1):
                            self.box_color(self.player1_x+1,self.player1_y-1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2):
                    self.box_color(self.player1_x,self.player1_y-1) #プレイヤー飛び越えを行わない

            #マスのカラー変更-右
            if self.player1_x+1 == self.player2_x and self.player1_y == self.player2_y and(not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x+2] == 1 or self.wall_list[self.player1_y+1][self.player1_x+2] == 1):
                        self.box_color(self.player1_x+2,self.player1_y) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player1_y][self.player1_x+1] == 2 or self.wall_list[self.player1_y][self.player1_x+2] == 2):
                            self.box_color(self.player1_x+1,self.player1_y-1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player1_y+1][self.player1_x+1] == 2 or self.wall_list[self.player1_y+1][self.player1_x+2] == 2):
                            self.box_color(self.player1_x+1,self.player1_y+1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1):
                    self.box_color(self.player1_x+1,self.player1_y) #プレイヤー飛び越えを行わない

            #マスのカラー変更-下
            if self.player1_x == self.player2_x and self.player1_y + 1 == self.player2_y and (not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y+2][self.player1_x] == 2) and (not self.wall_list[self.player1_y+2][self.player1_x+1] == 2):
                        self.box_color(self.player1_x,self.player1_y+2) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player1_y+1][self.player1_x+1] == 1 or self.wall_list[self.player1_y+2][self.player1_x+1] == 1):
                            self.box_color(self.player1_x+1,self.player1_y+1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player1_y+1][self.player1_x] == 1 or self.wall_list[self.player1_y+2][self.player1_x] == 1):
                            self.box_color(self.player1_x-1,self.player1_y+1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2):
                    self.box_color(self.player1_x,self.player1_y+1) #プレイヤー飛び越えを行わない

            #マスのカラー変更-左
            if self.player1_x-1 == self.player2_x and self.player1_y == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x-1] == 1 or self.wall_list[self.player1_y+1][self.player1_x-1] == 1):
                        self.box_color(self.player1_x-2,self.player1_y) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x-1] == 2):
                            self.box_color(self.player1_x-1,self.player1_y+1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x-1] == 2):
                            self.box_color(self.player1_x-1,self.player1_y-1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1):
                    self.box_color(self.player1_x-1,self.player1_y) #プレイヤー飛び越えを行わない

            
            

            #矢印のカラー変更
            if self.player1_vector == 1: #and self.player1_y >= 1:
                if self.player1_x == self.player2_x and self.player1_y - 1 == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y-1][self.player1_x] == 2) and (not self.wall_list[self.player1_y-1][self.player1_x+1] == 2):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁なし

                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y-1][self.player1_x] == 1 or self.wall_list[self.player1_y][self.player1_x] == 1)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y-1][self.player1_x+1] == 1 or self.wall_list[self.player1_y][self.player1_x+1] == 1)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x+1] == 2):
                    self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行わない

                else:
                    self.arrow_color = self.arrow_color_cant


                

            elif self.player1_vector == 2: #and self.player1_y >= 1:
                if self.player1_x+1 == self.player2_x and self.player1_y == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x+2] == 1 or self.wall_list[self.player1_y+1][self.player1_x+2] == 1):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁なし

                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y][self.player1_x+1] == 2 or self.wall_list[self.player1_y][self.player1_x+2] == 2)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y+1][self.player1_x+1] == 2 or self.wall_list[self.player1_y+1][self.player1_x+2] == 2)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player1_y][self.player1_x+1] == 1 or self.wall_list[self.player1_y+1][self.player1_x+1] == 1):
                    self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant
            elif self.player1_vector == 3: #and self.player1_y >= 1:
                if self.player1_x == self.player2_x and self.player1_y + 1 == self.player2_y and (not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2)):
                    if (not self.wall_list[self.player1_y+2][self.player1_x] == 2) and (not self.wall_list[self.player1_y+2][self.player1_x+1] == 2):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁なし

                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y+1][self.player1_x+1] == 1 or self.wall_list[self.player1_y+2][self.player1_x+1] == 1)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y+1][self.player1_x] == 1 or self.wall_list[self.player1_y+2][self.player1_x] == 1)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x+1] == 2):
                    self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant
            elif self.player1_vector == 4: #and self.player1_y >= 1:
                if self.player1_x-1 == self.player2_x and self.player1_y == self.player2_y and (not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1)):
                    if not(self.wall_list[self.player1_y][self.player1_x-1] == 1 or self.wall_list[self.player1_y+1][self.player1_x-1] == 1):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁なし

                    elif self.player1_vector_dia == 1 and (not (self.wall_list[self.player1_y+1][self.player1_x] == 2 or self.wall_list[self.player1_y+1][self.player1_x-1] == 2)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    elif self.player1_vector_dia == 2 and (not (self.wall_list[self.player1_y][self.player1_x] == 2 or self.wall_list[self.player1_y][self.player1_x-1] == 2)):
                        self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player1_y][self.player1_x] == 1 or self.wall_list[self.player1_y+1][self.player1_x] == 1):
                    self.arrow_color = self.arrow_color_player1 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant

                
        elif self.player_now == 2:


            #マスのカラー変更-上
            if self.player2_x == self.player1_x and self.player2_y - 1 == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y-1][self.player2_x] == 2) and (not self.wall_list[self.player2_y-1][self.player2_x+1] == 2):
                        self.box_color(self.player2_x,self.player2_y-2) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player2_y-1][self.player2_x] == 1 or self.wall_list[self.player2_y][self.player2_x] == 1):
                            self.box_color(self.player2_x-1,self.player2_y-1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player2_y-1][self.player2_x+1] == 1 or self.wall_list[self.player2_y][self.player2_x+1] == 1):
                            self.box_color(self.player2_x+1,self.player2_y-1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2):
                    self.box_color(self.player2_x,self.player2_y-1) #プレイヤー飛び越えを行わない

            #マスのカラー変更-右
            if self.player2_x+1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x+2] == 1 or self.wall_list[self.player2_y+1][self.player2_x+2] == 1):
                        self.box_color(self.player2_x+2,self.player2_y) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player2_y][self.player2_x+1] == 2 or self.wall_list[self.player2_y][self.player2_x+2] == 2):
                            self.box_color(self.player2_x+1,self.player2_y-1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player2_y+1][self.player2_x+1] == 2 or self.wall_list[self.player2_y+1][self.player2_x+2] == 2):
                            self.box_color(self.player2_x+1,self.player2_y+1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1):
                    self.box_color(self.player2_x+1,self.player2_y) #プレイヤー飛び越えを行わない

            #マスのカラー変更-下
            if self.player2_x == self.player1_x and self.player2_y + 1 == self.player1_y and (not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y+2][self.player2_x] == 2) and (not self.wall_list[self.player2_y+2][self.player2_x+1] == 2):
                        self.box_color(self.player2_x,self.player2_y+2) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player2_y+1][self.player2_x+1] == 1 or self.wall_list[self.player2_y+2][self.player2_x+1] == 1):
                            self.box_color(self.player2_x+1,self.player2_y+1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player2_y+1][self.player2_x] == 1 or self.wall_list[self.player2_y+2][self.player2_x] == 1):
                            self.box_color(self.player2_x-1,self.player2_y+1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2):
                    self.box_color(self.player2_x,self.player2_y+1) #プレイヤー飛び越えを行わない

            #マスのカラー変更-左
            if self.player2_x-1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x-1] == 1 or self.wall_list[self.player2_y+1][self.player2_x-1] == 1):
                        self.box_color(self.player2_x-2,self.player2_y) #プレイヤー飛び越えを行う、壁なし

                    else:
                        if not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x-1] == 2):
                            self.box_color(self.player2_x-1,self.player2_y+1) #プレイヤー飛び越えを行う、壁あり

                        if not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x-1] == 2):
                            self.box_color(self.player2_x-1,self.player2_y-1) #プレイヤー飛び越えを行う、壁あり

                    
            elif not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1):
                    self.box_color(self.player2_x-1,self.player2_y) #プレイヤー飛び越えを行わない
            

            #矢印のカラー変更
            if self.player2_vector == 1: #and self.player1_y >= 1:
                if self.player2_x == self.player1_x and self.player2_y - 1 == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y-1][self.player2_x] == 2) and (not self.wall_list[self.player2_y-1][self.player2_x+1] == 2):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁なし

                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y-1][self.player2_x] == 1 or self.wall_list[self.player2_y][self.player2_x] == 1)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y-1][self.player2_x+1] == 1 or self.wall_list[self.player2_y][self.player2_x+1] == 1)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x+1] == 2):
                    self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant

                

            elif self.player2_vector == 2: #and self.player2_y >= 1:
                if self.player2_x+1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x+2] == 1 or self.wall_list[self.player2_y+1][self.player2_x+2] == 1):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁なし

                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y][self.player2_x+1] == 2 or self.wall_list[self.player2_y][self.player2_x+2] == 2)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y+1][self.player2_x+1] == 2 or self.wall_list[self.player2_y+1][self.player2_x+2] == 2)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player2_y][self.player2_x+1] == 1 or self.wall_list[self.player2_y+1][self.player2_x+1] == 1):
                    self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant

            elif self.player2_vector == 3: #and self.player2_y >= 1:
                if self.player2_x == self.player1_x and self.player2_y + 1 == self.player1_y and (not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2)):
                    if (not self.wall_list[self.player2_y+2][self.player2_x] == 2) and (not self.wall_list[self.player2_y+2][self.player2_x+1] == 2):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁なし

                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y+1][self.player2_x+1] == 1 or self.wall_list[self.player2_y+2][self.player2_x+1] == 1)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y+1][self.player2_x] == 1 or self.wall_list[self.player2_y+2][self.player2_x] == 1)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x+1] == 2):
                    self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant
            elif self.player2_vector == 4: #and self.player2_y >= 1:
                if self.player2_x-1 == self.player1_x and self.player2_y == self.player1_y and (not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1)):
                    if not(self.wall_list[self.player2_y][self.player2_x-1] == 1 or self.wall_list[self.player2_y+1][self.player2_x-1] == 1):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁なし

                    elif self.player2_vector_dia == 1 and (not (self.wall_list[self.player2_y+1][self.player2_x] == 2 or self.wall_list[self.player2_y+1][self.player2_x-1] == 2)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    elif self.player2_vector_dia == 2 and (not (self.wall_list[self.player2_y][self.player2_x] == 2 or self.wall_list[self.player2_y][self.player2_x-1] == 2)):
                        self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行う、壁あり

                    else:
                        self.arrow_color = self.arrow_color_cant
                elif not (self.wall_list[self.player2_y][self.player2_x] == 1 or self.wall_list[self.player2_y+1][self.player2_x] == 1):
                    self.arrow_color = self.arrow_color_player2 #プレイヤー飛び越えを行わない
                else:
                    self.arrow_color = self.arrow_color_cant

        for x in range(8):
            for y in range(8):
                if self.wall_list[y+1][x+1] == 1:
                    pyxel.rect(39+x*38,7+y*38,5,69,10)
                elif self.wall_list[y+1][x+1] == 2:
                    pyxel.rect(7+x*38,39+y*38,69,5,10)

        if self.player_now == 1:
            
            if self.player1_vector == 1:
                if self.player1_vector_dia == 0:
                    #上矢印    
                    pyxel.rect(18 + self.player1_x * 38,-5 + self.player1_y * 38,9,16,self.arrow_color)
                    pyxel.tri(13 + self.player1_x * 38,-4 + self.player1_y * 38,31 + self.player1_x * 38,-4 + self.player1_y * 38,22 + self.player1_x * 38,-13 + self.player1_y * 38,self.arrow_color)
                    pyxel.rect(19 + self.player1_x * 38,-4 + self.player1_y * 38,7,14,7)
                    pyxel.tri(16 + self.player1_x * 38,-5 + self.player1_y * 38,28 + self.player1_x * 38,-5 + self.player1_y * 38,22 + self.player1_x * 38,-11 + self.player1_y * 38,7)
                    self.cross__arrow_draw(22 + self.player1_x * 38,2 + self.player1_y * 38)
                elif self.player1_vector_dia == 1:
                    #左上矢印    
                    pyxel.tri(-3 + self.player1_x * 38,3 + self.player1_y * 38,3 + self.player1_x * 38,-3 + self.player1_y * 38,7+ self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player1_x * 38,-3 + self.player1_y * 38,13 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,-6 + self.player1_y * 38,-6 + self.player1_x * 38,-6 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player1_x * 38,1 + self.player1_y * 38,1 + self.player1_x * 38,-3 + self.player1_y * 38,7 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(1 + self.player1_x * 38,-3 + self.player1_y * 38,11 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(-5 + self.player1_x * 38,4 + self.player1_y * 38,4 + self.player1_x * 38,-5 + self.player1_y * 38,-5 + self.player1_x * 38,-5 + self.player1_y * 38,7)
                    self.cross__arrow_draw(5 + self.player1_x * 38,5 + self.player1_y * 38)
                elif self.player1_vector_dia == 2:
                    #右上矢印    
                    pyxel.tri(47 + self.player1_x * 38,3 + self.player1_y * 38,41 + self.player1_x * 38,-3 + self.player1_y * 38,37+ self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player1_x * 38,-3 + self.player1_y * 38,31 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,-6 + self.player1_y * 38,50 + self.player1_x * 38,-6 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player1_x * 38,1 + self.player1_y * 38,43 + self.player1_x * 38,-3 + self.player1_y * 38,37 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(43 + self.player1_x * 38,-3 + self.player1_y * 38,33 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(49 + self.player1_x * 38,4 + self.player1_y * 38,40 + self.player1_x * 38,-5 + self.player1_y * 38,49 + self.player1_x * 38,-5 + self.player1_y * 38,7)
                    self.cross__arrow_draw(39 + self.player1_x * 38,5 + self.player1_y * 38)
            elif self.player1_vector == 2:
                if self.player1_vector_dia == 0:
                    #右矢印    
                    pyxel.rect(34 + self.player1_x * 38,18 + self.player1_y * 38,16,9,self.arrow_color)
                    pyxel.tri(48 + self.player1_x * 38,13 + self.player1_y * 38,48 + self.player1_x * 38,31 + self.player1_y * 38,57 + self.player1_x * 38,22 + self.player1_y * 38,self.arrow_color)
                    pyxel.rect(35 + self.player1_x * 38,19 + self.player1_y * 38,14,7,7)
                    pyxel.tri(49 + self.player1_x * 38,16 + self.player1_y * 38,49 + self.player1_x * 38,28 + self.player1_y * 38,55 + self.player1_x * 38,22 + self.player1_y * 38,7)
                    self.cross__arrow_draw(42 + self.player1_x * 38,22 + self.player1_y * 38)
                elif self.player1_vector_dia == 1:
                    #右上矢印    
                    pyxel.tri(47 + self.player1_x * 38,3 + self.player1_y * 38,41 + self.player1_x * 38,-3 + self.player1_y * 38,37+ self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player1_x * 38,-3 + self.player1_y * 38,31 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,-6 + self.player1_y * 38,50 + self.player1_x * 38,-6 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player1_x * 38,1 + self.player1_y * 38,43 + self.player1_x * 38,-3 + self.player1_y * 38,37 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(43 + self.player1_x * 38,-3 + self.player1_y * 38,33 + self.player1_x * 38,7 + self.player1_y * 38,37 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(49 + self.player1_x * 38,4 + self.player1_y * 38,40 + self.player1_x * 38,-5 + self.player1_y * 38,49 + self.player1_x * 38,-5 + self.player1_y * 38,7)
                    self.cross__arrow_draw(39 + self.player1_x * 38,5 + self.player1_y * 38)
                elif self.player1_vector_dia == 2:
                    #右下矢印    
                    pyxel.tri(47 + self.player1_x * 38,41 + self.player1_y * 38,41 + self.player1_x * 38,47 + self.player1_y * 38,37+ self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player1_x * 38,47 + self.player1_y * 38,31 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,50 + self.player1_y * 38,50 + self.player1_x * 38,50 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player1_x * 38,43 + self.player1_y * 38,43 + self.player1_x * 38,47 + self.player1_y * 38,37 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(43 + self.player1_x * 38,47 + self.player1_y * 38,33 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(49 + self.player1_x * 38,40 + self.player1_y * 38,40 + self.player1_x * 38,49 + self.player1_y * 38,49 + self.player1_x * 38,49 + self.player1_y * 38,7)
                    self.cross__arrow_draw(39 + self.player1_x * 38,39 + self.player1_y * 38)
            elif self.player1_vector == 3:
                if self.player1_vector_dia == 0:
                    #下矢印    
                    pyxel.rect(18 + self.player1_x * 38,34 + self.player1_y * 38,9,16,self.arrow_color)
                    pyxel.tri(13 + self.player1_x * 38,48 + self.player1_y * 38,31 + self.player1_x * 38,48 + self.player1_y * 38,22 + self.player1_x * 38,57 + self.player1_y * 38,self.arrow_color)
                    pyxel.rect(19 + self.player1_x * 38,35 + self.player1_y * 38,7,14,7)
                    pyxel.tri(16 + self.player1_x * 38,49 + self.player1_y * 38,28 + self.player1_x * 38,49 + self.player1_y * 38,22 + self.player1_x * 38,55 + self.player1_y * 38,7)
                    self.cross__arrow_draw(22 + self.player1_x * 38,42 + self.player1_y * 38)
                elif self.player1_vector_dia == 1:
                    #右下矢印    
                    pyxel.tri(47 + self.player1_x * 38,41 + self.player1_y * 38,41 + self.player1_x * 38,47 + self.player1_y * 38,37+ self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player1_x * 38,47 + self.player1_y * 38,31 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,50 + self.player1_y * 38,50 + self.player1_x * 38,50 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player1_x * 38,43 + self.player1_y * 38,43 + self.player1_x * 38,47 + self.player1_y * 38,37 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(43 + self.player1_x * 38,47 + self.player1_y * 38,33 + self.player1_x * 38,37 + self.player1_y * 38,37 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(49 + self.player1_x * 38,40 + self.player1_y * 38,40 + self.player1_x * 38,49 + self.player1_y * 38,49 + self.player1_x * 38,49 + self.player1_y * 38,7)
                    self.cross__arrow_draw(39 + self.player1_x * 38,39 + self.player1_y * 38)
                elif self.player1_vector_dia == 2:
                    #左下矢印    
                    pyxel.tri(-3 + self.player1_x * 38,41 + self.player1_y * 38,3 + self.player1_x * 38,47 + self.player1_y * 38,7+ self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player1_x * 38,47 + self.player1_y * 38,13 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,50 + self.player1_y * 38,-6 + self.player1_x * 38,50 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player1_x * 38,43 + self.player1_y * 38,1 + self.player1_x * 38,47 + self.player1_y * 38,7 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(1 + self.player1_x * 38,47 + self.player1_y * 38,11 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(-5 + self.player1_x * 38,40 + self.player1_y * 38,4 + self.player1_x * 38,49 + self.player1_y * 38,-5 + self.player1_x * 38,49 + self.player1_y * 38,7)
                    self.cross__arrow_draw(5 + self.player1_x * 38,39 + self.player1_y * 38)
            elif self.player1_vector == 4:
                if self.player1_vector_dia == 0:
                    #左矢印    
                    pyxel.rect(-5 + self.player1_x * 38,18 + self.player1_y * 38,16,9,self.arrow_color)
                    pyxel.tri(-4 + self.player1_x * 38,13 + self.player1_y * 38,-4 + self.player1_x * 38,31 + self.player1_y * 38,-13 + self.player1_x * 38,22 + self.player1_y * 38,self.arrow_color)
                    pyxel.rect(-4 + self.player1_x * 38,19 + self.player1_y * 38,14,7,7)
                    pyxel.tri(-5 + self.player1_x * 38,16 + self.player1_y * 38,-5 + self.player1_x * 38,28 + self.player1_y * 38,-11 + self.player1_x * 38,22 + self.player1_y * 38,7)
                    self.cross__arrow_draw(2 + self.player1_x * 38,22 + self.player1_y * 38)
                elif self.player1_vector_dia == 1:
                    #左下矢印    
                    pyxel.tri(-3 + self.player1_x * 38,41 + self.player1_y * 38,3 + self.player1_x * 38,47 + self.player1_y * 38,7+ self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player1_x * 38,47 + self.player1_y * 38,13 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,31 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,50 + self.player1_y * 38,-6 + self.player1_x * 38,50 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player1_x * 38,43 + self.player1_y * 38,1 + self.player1_x * 38,47 + self.player1_y * 38,7 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(1 + self.player1_x * 38,47 + self.player1_y * 38,11 + self.player1_x * 38,37 + self.player1_y * 38,7 + self.player1_x * 38,33 + self.player1_y * 38,7)
                    pyxel.tri(-5 + self.player1_x * 38,40 + self.player1_y * 38,4 + self.player1_x * 38,49 + self.player1_y * 38,-5 + self.player1_x * 38,49 + self.player1_y * 38,7)
                    self.cross__arrow_draw(5 + self.player1_x * 38,39 + self.player1_y * 38)
                elif self.player1_vector_dia == 2:
                    #左上矢印    
                    pyxel.tri(-3 + self.player1_x * 38,3 + self.player1_y * 38,3 + self.player1_x * 38,-3 + self.player1_y * 38,7+ self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player1_x * 38,-3 + self.player1_y * 38,13 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,13 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,-6 + self.player1_y * 38,-6 + self.player1_x * 38,-6 + self.player1_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player1_x * 38,1 + self.player1_y * 38,1 + self.player1_x * 38,-3 + self.player1_y * 38,7 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(1 + self.player1_x * 38,-3 + self.player1_y * 38,11 + self.player1_x * 38,7 + self.player1_y * 38,7 + self.player1_x * 38,11 + self.player1_y * 38,7)
                    pyxel.tri(-5 + self.player1_x * 38,4 + self.player1_y * 38,4 + self.player1_x * 38,-5 + self.player1_y * 38,-5 + self.player1_x * 38,-5 + self.player1_y * 38,7)
                    self.cross__arrow_draw(5 + self.player1_x * 38,5 + self.player1_y * 38)

        elif self.player_now == 2:
            
            if self.player2_vector == 1:
                if self.player2_vector_dia == 0:
                    #上矢印    
                    pyxel.rect(18 + self.player2_x * 38,-5 + self.player2_y * 38,9,16,self.arrow_color)
                    pyxel.tri(13 + self.player2_x * 38,-4 + self.player2_y * 38,31 + self.player2_x * 38,-4 + self.player2_y * 38,22 + self.player2_x * 38,-13 + self.player2_y * 38,self.arrow_color)
                    pyxel.rect(19 + self.player2_x * 38,-4 + self.player2_y * 38,7,14,7)
                    pyxel.tri(16 + self.player2_x * 38,-5 + self.player2_y * 38,28 + self.player2_x * 38,-5 + self.player2_y * 38,22 + self.player2_x * 38,-11 + self.player2_y * 38,7)
                    self.cross__arrow_draw(22 + self.player2_x * 38,2 + self.player2_y * 38)
                elif self.player2_vector_dia == 1:
                    #左上矢印    
                    pyxel.tri(-3 + self.player2_x * 38,3 + self.player2_y * 38,3 + self.player2_x * 38,-3 + self.player2_y * 38,7+ self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player2_x * 38,-3 + self.player2_y * 38,13 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,-6 + self.player2_y * 38,-6 + self.player2_x * 38,-6 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player2_x * 38,1 + self.player2_y * 38,1 + self.player2_x * 38,-3 + self.player2_y * 38,7 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(1 + self.player2_x * 38,-3 + self.player2_y * 38,11 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(-5 + self.player2_x * 38,4 + self.player2_y * 38,4 + self.player2_x * 38,-5 + self.player2_y * 38,-5 + self.player2_x * 38,-5 + self.player2_y * 38,7)
                    self.cross__arrow_draw(5 + self.player2_x * 38,5 + self.player2_y * 38)
                elif self.player2_vector_dia == 2:
                    #右上矢印    
                    pyxel.tri(47 + self.player2_x * 38,3 + self.player2_y * 38,41 + self.player2_x * 38,-3 + self.player2_y * 38,37+ self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player2_x * 38,-3 + self.player2_y * 38,31 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,-6 + self.player2_y * 38,50 + self.player2_x * 38,-6 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player2_x * 38,1 + self.player2_y * 38,43 + self.player2_x * 38,-3 + self.player2_y * 38,37 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(43 + self.player2_x * 38,-3 + self.player2_y * 38,33 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(49 + self.player2_x * 38,4 + self.player2_y * 38,40 + self.player2_x * 38,-5 + self.player2_y * 38,49 + self.player2_x * 38,-5 + self.player2_y * 38,7)
                    self.cross__arrow_draw(39 + self.player2_x * 38,5 + self.player2_y * 38)
            elif self.player2_vector == 2:
                if self.player2_vector_dia == 0:
                    #右矢印    
                    pyxel.rect(34 + self.player2_x * 38,18 + self.player2_y * 38,16,9,self.arrow_color)
                    pyxel.tri(48 + self.player2_x * 38,13 + self.player2_y * 38,48 + self.player2_x * 38,31 + self.player2_y * 38,57 + self.player2_x * 38,22 + self.player2_y * 38,self.arrow_color)
                    pyxel.rect(35 + self.player2_x * 38,19 + self.player2_y * 38,14,7,7)
                    pyxel.tri(49 + self.player2_x * 38,16 + self.player2_y * 38,49 + self.player2_x * 38,28 + self.player2_y * 38,55 + self.player2_x * 38,22 + self.player2_y * 38,7)
                    self.cross__arrow_draw(42 + self.player2_x * 38,22 + self.player2_y * 38)
                elif self.player2_vector_dia == 1:
                    #右上矢印    
                    pyxel.tri(47 + self.player2_x * 38,3 + self.player2_y * 38,41 + self.player2_x * 38,-3 + self.player2_y * 38,37+ self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player2_x * 38,-3 + self.player2_y * 38,31 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,-6 + self.player2_y * 38,50 + self.player2_x * 38,-6 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player2_x * 38,1 + self.player2_y * 38,43 + self.player2_x * 38,-3 + self.player2_y * 38,37 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(43 + self.player2_x * 38,-3 + self.player2_y * 38,33 + self.player2_x * 38,7 + self.player2_y * 38,37 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(49 + self.player2_x * 38,4 + self.player2_y * 38,40 + self.player2_x * 38,-5 + self.player2_y * 38,49 + self.player2_x * 38,-5 + self.player2_y * 38,7)
                    self.cross__arrow_draw(39 + self.player2_x * 38,5 + self.player2_y * 38)
                elif self.player2_vector_dia == 2:
                    #右下矢印    
                    pyxel.tri(47 + self.player2_x * 38,41 + self.player2_y * 38,41 + self.player2_x * 38,47 + self.player2_y * 38,37+ self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player2_x * 38,47 + self.player2_y * 38,31 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,50 + self.player2_y * 38,50 + self.player2_x * 38,50 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player2_x * 38,43 + self.player2_y * 38,43 + self.player2_x * 38,47 + self.player2_y * 38,37 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(43 + self.player2_x * 38,47 + self.player2_y * 38,33 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(49 + self.player2_x * 38,40 + self.player2_y * 38,40 + self.player2_x * 38,49 + self.player2_y * 38,49 + self.player2_x * 38,49 + self.player2_y * 38,7)
                    self.cross__arrow_draw(39 + self.player2_x * 38,39 + self.player2_y * 38)
            elif self.player2_vector == 3:
                if self.player2_vector_dia == 0:
                    #下矢印    
                    pyxel.rect(18 + self.player2_x * 38,34 + self.player2_y * 38,9,16,self.arrow_color)
                    pyxel.tri(13 + self.player2_x * 38,48 + self.player2_y * 38,31 + self.player2_x * 38,48 + self.player2_y * 38,22 + self.player2_x * 38,57 + self.player2_y * 38,self.arrow_color)
                    pyxel.rect(19 + self.player2_x * 38,35 + self.player2_y * 38,7,14,7)
                    pyxel.tri(16 + self.player2_x * 38,49 + self.player2_y * 38,28 + self.player2_x * 38,49 + self.player2_y * 38,22 + self.player2_x * 38,55 + self.player2_y * 38,7)
                    self.cross__arrow_draw(22 + self.player2_x * 38,42 + self.player2_y * 38)
                elif self.player2_vector_dia == 1:
                    #右下矢印    
                    pyxel.tri(47 + self.player2_x * 38,41 + self.player2_y * 38,41 + self.player2_x * 38,47 + self.player2_y * 38,37+ self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(41 + self.player2_x * 38,47 + self.player2_y * 38,31 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(50 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,50 + self.player2_y * 38,50 + self.player2_x * 38,50 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(47 + self.player2_x * 38,43 + self.player2_y * 38,43 + self.player2_x * 38,47 + self.player2_y * 38,37 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(43 + self.player2_x * 38,47 + self.player2_y * 38,33 + self.player2_x * 38,37 + self.player2_y * 38,37 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(49 + self.player2_x * 38,40 + self.player2_y * 38,40 + self.player2_x * 38,49 + self.player2_y * 38,49 + self.player2_x * 38,49 + self.player2_y * 38,7)
                    self.cross__arrow_draw(39 + self.player2_x * 38,39 + self.player2_y * 38)
                elif self.player2_vector_dia == 2:
                    #左下矢印    
                    pyxel.tri(-3 + self.player2_x * 38,41 + self.player2_y * 38,3 + self.player2_x * 38,47 + self.player2_y * 38,7+ self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player2_x * 38,47 + self.player2_y * 38,13 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,50 + self.player2_y * 38,-6 + self.player2_x * 38,50 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player2_x * 38,43 + self.player2_y * 38,1 + self.player2_x * 38,47 + self.player2_y * 38,7 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(1 + self.player2_x * 38,47 + self.player2_y * 38,11 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(-5 + self.player2_x * 38,40 + self.player2_y * 38,4 + self.player2_x * 38,49 + self.player2_y * 38,-5 + self.player2_x * 38,49 + self.player2_y * 38,7)
                    self.cross__arrow_draw(5 + self.player2_x * 38,39 + self.player2_y * 38)
            elif self.player2_vector == 4:
                if self.player2_vector_dia == 0:
                    #左矢印    
                    pyxel.rect(-5 + self.player2_x * 38,18 + self.player2_y * 38,16,9,self.arrow_color)
                    pyxel.tri(-4 + self.player2_x * 38,13 + self.player2_y * 38,-4 + self.player2_x * 38,31 + self.player2_y * 38,-13 + self.player2_x * 38,22 + self.player2_y * 38,self.arrow_color)
                    pyxel.rect(-4 + self.player2_x * 38,19 + self.player2_y * 38,14,7,7)
                    pyxel.tri(-5 + self.player2_x * 38,16 + self.player2_y * 38,-5 + self.player2_x * 38,28 + self.player2_y * 38,-11 + self.player2_x * 38,22 + self.player2_y * 38,7)
                    self.cross__arrow_draw(2 + self.player2_x * 38,22 + self.player2_y * 38)
                elif self.player2_vector_dia == 1:
                    #左下矢印    
                    pyxel.tri(-3 + self.player2_x * 38,41 + self.player2_y * 38,3 + self.player2_x * 38,47 + self.player2_y * 38,7+ self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player2_x * 38,47 + self.player2_y * 38,13 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,31 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,50 + self.player2_y * 38,-6 + self.player2_x * 38,50 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player2_x * 38,43 + self.player2_y * 38,1 + self.player2_x * 38,47 + self.player2_y * 38,7 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(1 + self.player2_x * 38,47 + self.player2_y * 38,11 + self.player2_x * 38,37 + self.player2_y * 38,7 + self.player2_x * 38,33 + self.player2_y * 38,7)
                    pyxel.tri(-5 + self.player2_x * 38,40 + self.player2_y * 38,4 + self.player2_x * 38,49 + self.player2_y * 38,-5 + self.player2_x * 38,49 + self.player2_y * 38,7)
                    self.cross__arrow_draw(5 + self.player2_x * 38,39 + self.player2_y * 38)
                elif self.player2_vector_dia == 2:
                    #左上矢印    
                    pyxel.tri(-3 + self.player2_x * 38,3 + self.player2_y * 38,3 + self.player2_x * 38,-3 + self.player2_y * 38,7+ self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(3 + self.player2_x * 38,-3 + self.player2_y * 38,13 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,13 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-6 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,-6 + self.player2_y * 38,-6 + self.player2_x * 38,-6 + self.player2_y * 38,self.arrow_color)
                    pyxel.tri(-3 + self.player2_x * 38,1 + self.player2_y * 38,1 + self.player2_x * 38,-3 + self.player2_y * 38,7 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(1 + self.player2_x * 38,-3 + self.player2_y * 38,11 + self.player2_x * 38,7 + self.player2_y * 38,7 + self.player2_x * 38,11 + self.player2_y * 38,7)
                    pyxel.tri(-5 + self.player2_x * 38,4 + self.player2_y * 38,4 + self.player2_x * 38,-5 + self.player2_y * 38,-5 + self.player2_x * 38,-5 + self.player2_y * 38,7)
                    self.cross__arrow_draw(5 + self.player2_x * 38,5 + self.player2_y * 38)

        if self.install_mode == 1:
            for x in range(8):
                for y in range(8):
                    if self.wall_list[y+1][x+1] == 0 and (not(self.wall_list[y][x+1] == 1 or self.wall_list[y+2][x+1] == 1)) and (not(x+1==self.wall_x and y+1==self.wall_y)) and self.wall_can(y+1,x+1,self.install_mode,False):
                        pyxel.rectb(38+x*38,38+y*38,7,7,11)

            if self.wall_list[self.wall_y][self.wall_x] == 0 and (not(self.wall_list[self.wall_y-1][self.wall_x] == 1 or self.wall_list[self.wall_y+1][self.wall_x] == 1)) and self.wall_can(self.wall_y,self.wall_x,self.install_mode):
                if self.player_now == 1:
                    pyxel.rectb(0+self.wall_x*38,-31+self.wall_y*38,7,69,12)
                    pyxel.rectb(1+self.wall_x*38,-30+self.wall_y*38,5,67,12)
                elif self.player_now == 2:
                    pyxel.rectb(0+self.wall_x*38,-31+self.wall_y*38,7,69,14)
                    pyxel.rectb(1+self.wall_x*38,-30+self.wall_y*38,5,67,14)
            else:
                pyxel.rectb(0+self.wall_x*38,-31+self.wall_y*38,7,69,13)
                pyxel.rectb(1+self.wall_x*38,-30+self.wall_y*38,5,67,13)
                self.cross__wall_draw(3+self.wall_x*38,3+self.wall_y*38)

            
        elif self.install_mode == 2:
            for x in range(8):
                for y in range(8):
                    if self.wall_list[y+1][x+1] == 0 and (not(self.wall_list[y+1][x] == 2 or self.wall_list[y+1][x+2] == 2)) and (not(x+1==self.wall_x and y+1==self.wall_y)) and self.wall_can(y+1,x+1,self.install_mode,False):
                        pyxel.rectb(38+x*38,38+y*38,7,7,9)

            if self.wall_list[self.wall_y][self.wall_x] == 0 and (not(self.wall_list[self.wall_y][self.wall_x-1] == 2 or self.wall_list[self.wall_y][self.wall_x+1] == 2)) and self.wall_can(self.wall_y,self.wall_x,self.install_mode):
                if self.player_now == 1:
                    pyxel.rectb(-31+self.wall_x*38,0+self.wall_y*38,69,7,12)
                    pyxel.rectb(-30+self.wall_x*38,1+self.wall_y*38,67,5,12)
                elif self.player_now == 2:
                    pyxel.rectb(-31+self.wall_x*38,0+self.wall_y*38,69,7,14)
                    pyxel.rectb(-30+self.wall_x*38,1+self.wall_y*38,67,5,14)
            else:
                pyxel.rectb(-31+self.wall_x*38,0+self.wall_y*38,69,7,13)
                pyxel.rectb(-30+self.wall_x*38,1+self.wall_y*38,67,5,13)
                self.cross__wall_draw(3+self.wall_x*38,3+self.wall_y*38)
    
      #pyxel.text(100,100,str(self.wall_list_tent[4]),0)
      #pyxel.text(100,110,str(self.wall_list[4]),0)
      #デバッグ用


Quoridor()