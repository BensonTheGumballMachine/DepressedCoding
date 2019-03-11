
from random import randint

class Character:
  def __init__(self):
    self.name = ""
    self.health = 1
    self.health_max = 1
  def do_damage(self, enemy):
    damage = min(
        max(randint(0, self.health) - randint(0, enemy.health), 0),
        enemy.health)
    enemy.health = enemy.health - damage
    if damage == 0: print "%s evades %s's attack." % (enemy.name, self.name)
    else: print "%s hurts %s!" % (self.name, enemy.name)
    return enemy.health <= 0

class Enemy(Character):
  def __init__(self, player):
    Character.__init__(self)
    enemy_name1 = randint(0,7)
    ex = randint(3,player.health_max)
    if enemy_name1 == 0:
        en = "super mutant"
        eh = ex +3
    elif enemy_name1 == 1:
        en = "raider"
        eh = ex
    elif enemy_name1 == 2:
        en = "some fuckin rat"
        eh = ex - 1
    elif enemy_name1 == 3 :
        en = "Brother Roman"
        eh = ex + 2
    elif enemy_name1 == 4 :
        en = "Solider Boy "
        eh = ex + 3
    elif enemy_name1 == 5:
        en = "nasty ass ghoul"
        eh = ex +1
    elif enemy_name1 == 6:
        en = "clawmonster"
        eh = ex + 4
    elif enemy_name1 == 7:
        en = "reddit lurker"
        eh = ex +1
    self.name = "%s" % (en)
    self.health = eh
class Player(Character):
  def __init__(self):
    Character.__init__(self)
    self.state = 'normal'
    self.health = 10
    self.health_max = 10
  def quit(self):
    print "%s can't find the way back home, and dies of starvation.\nR.I.P." % self.name
    self.health = 0
  def help(self): print Commands.keys()
  def status(self): print "%s's health: %d/%d" % (self.name, self.health, self.health_max)
  def tired(self):
    print "%s feels tired." % self.name
    self.health = max(1, self.health - 1)
  def rest(self):
    if self.state != 'normal': print "%s can't rest now!" % self.name; self.enemy_attacks()
    else:
      print "%s rests." % self.name
      if randint(0, 1):
        self.enemy = Enemy(self)
        print "%s is rudely awakened by %s!" % (self.name, self.enemy.name)
        self.state = 'fight'
        self.enemy_attacks()
      else:
        if self.health < self.health_max:
          self.health = self.health + 1
        else: print "%s slept too much." % self.name; self.health = self.health - 1
  def explore(self):
    if self.state != 'normal':
      print "%s is too busy right now!" % self.name
      self.enemy_attacks()
    else:
      print "%s explores the cave of teenage angst." % self.name
      if randint(0, 1):
        self.enemy = Enemy(self)
        print "%s encounters %s!" % (self.name, self.enemy.name)
        self.state = 'fight'
      else:
        if randint(0, 1): self.tired()
  def flee(self):
    if self.state != 'fight': print "%s runs in circles for a while." % self.name; self.tired()
    else:
      if randint(1, self.health + 5) > randint(1, self.enemy.health):
        print "%s flees from %s." % (self.name, self.enemy.name)
        self.enemy = None
        self.state = 'normal'
      else: print "%s couldn't escape from %s!" % (self.name, self.enemy.name); self.enemy_attacks()
  def dance(self):
      if self.state != 'fight': print "%s dances to a happy tune in the distance." % self.name;self.tired()
      else:
          if randint(1 , self.health +90) > randint(1, self.enemy.health):
              print "%s dances in front of %s, %s is confused and leaves" % (self.name, self.enemy.name, self.enemy.name)
              self.enemy = None
              self.state = 'normal'
          else: print ("%s hated your fucking dance %s attacks") % (self.enemy.name , self.enemy.name); self.enemy_attacks()
  def attack(self):
    if self.state != 'fight': print "%s swats the air, without notable results." % self.name; self.tired()
    else:
      if self.do_damage(self.enemy):
        print "%s executes %s!" % (self.name, self.enemy.name)
        self.enemy = None
        self.state = 'normal'
        if randint(0, self.health) < 10:
          self.health = self.health + 1
          self.health_max = self.health_max + 1
          print "%s feels stronger!" % self.name
      else: self.enemy_attacks()
  def enemy_attacks(self):
    if self.enemy.do_damage(self): print "%s was slaughtered by %s!!!\nR.I.P." %(self.name, self.enemy.name)

Commands = {
  'quit': Player.quit,
  'help': Player.help,
  'status': Player.status,
  'rest': Player.rest,
  'explore': Player.explore,
  'flee': Player.flee,
  'attack': Player.attack,
  'dance' : Player.dance,
  }

p = Player()
p.name = raw_input("What is your character's name? ")
print "(type help to get a list of actions)\n"
print "%s enters a dark cave, searching for adventure." % p.name

while(p.health > 0):
  line = raw_input("> ")
  args = line.split()
  if len(args) > 0:
    commandFound = False
    for c in Commands.keys():
      if args[0] == c[:len(args[0])]:
        Commands[c](p)
        commandFound = True
        break
    if not commandFound:
      print "%s doesn't understand the suggestion." % p.name
