from time import sleep
import pyautogui
import pydirectinput


class Game:
  teamcheck = False
  leftleft, lefttop, leftwidth, leftheight = 481, 400, 474, 400
  rightleft, righttop, rightwidth, rightheight = 1024, 415, 400, 353

  def tier(tier: int):
    '''
    NOT WORKING!
    
    args:
      tier(int): 1-3 select what tier to use

    '''
    tierfinder=[]
    try:
      print(f'images/tier{tier}.png')
      position= pyautogui.locateOnScreen(f'images/tier{tier}.png', confidence=.2)
      if position != None:
        for pos in position:
          tierfinder.append(pos)
        pydirectinput.moveTo(tierfinder[0], tierfinder[1], tierfinder[2], tierfinder[3])
        pydirectinput.leftClick()
    except TypeError:
      print('not found')
      pass
  def start_game():
    '''
    Searches Screen for deploy button
    '''
    deploy_list=[]
    position = pyautogui.locateCenterOnScreen('images/deploy.png', confidence=.7)
    if not position == None:
      for pos in position:
        deploy_list.append(pos)
      else:
        pass
      #* deploy
      print('Deploy Button found.. ')
      pydirectinput.moveTo(deploy_list[0], deploy_list[1])
      pydirectinput.move(50, 0)
      pydirectinput.move(-70, 0)
      pydirectinput.click(button='left')
      global find_team_variable
      find_team_variable = 0
    else:
      pass
    
  def find_team():
    team_list=[]
    keyboard.press_and_release('tab')
    sleep(.1)
    scoreboardright = pyautogui.screenshot(region=(leftleft, lefttop, leftwidth, leftheight))
    scoreboardleft = pyautogui.screenshot(region=(rightleft, righttop, rightwidth, rightheight))
    scoreboardleft.save('left.png')
    scoreboardright.save('right.png')
    #! Left side of scoreboard
    try:
      for pos in pyautogui.locateOnScreen('images/username.png', confidence=0.9, region=(leftleft, lefttop, leftwidth, leftheight)):
        team_list.append(pos)
      pydirectinput.moveTo(team_list[0], team_list[1], team_list[2], team_list[3])
      keyboard.press_and_release('tab')
      print('username found Left Side')
      leftside = True
      return leftside
    except TypeError: 
      pass
    #! Right side of scoreboard
    try:
      for pos in pyautogui.locateOnScreen('images/username.png',confidence=.9, region=(rightleft, righttop, rightwidth, rightheight)):
        team_list.append(pos)
      pydirectinput.moveTo(team_list[0], team_list[1], team_list[2], team_list[3])
      sleep(.1)
      keyboard.press_and_release('tab')
      print('username found Right side')
      rightside = True
      return rightside
    except TypeError:
      print('username Not found')
      pass


  def aim_toggle_on():
    aimoff_list=[]
    try:
      for pos in pyautogui.locateCenterOnScreen('images/aimoff.png', confidence=0.9):
        aimoff_list.append(pos)
      else:
        pass

      print('aimoff found.. ')
      pydirectinput.moveTo(aimoff_list[0], aimoff_list[1])
      pydirectinput.moveRel(1, 0)
      pydirectinput.moveRel(-2, 0)
      pydirectinput.click(button='left')

    except TypeError:
      pass

  def death_screen():
    try:
      if not pyautogui.locateCenterOnScreen('images/shipdestroyed.png', confidence=0.9) == None:
        global find_team_variable
        find_team_variable = 0
        print('Death Screen found.. ')
      else:
        pass
    except TypeError:
      pass