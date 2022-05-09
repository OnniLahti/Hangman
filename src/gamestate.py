#Function that stores the different states of game in strings made from ASCII characters
def gameboard(tries):
    """
    It takes in a number of tries and returns a string that represents the gameboard
    
    :param tries: the number of tries the player has used
    """
    match tries:
        case 0:
            return """
  []    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
  []    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
  [][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
  []    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
  []    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

              ___________
              |         |
              |         |
              |
              |
              |
              |
              |
     _________|__________________
    /         |                 /|
   /                           / |
  /___________________________/  /
  |                           | /
  |___________________________|/
"""

        case 1:
            return """
  []    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
  []    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
  [][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
  []    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
  []    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

              ___________
              |         |
              |         |
              |         @
              |
              |
              |
              |
     _________|__________________
    /         |                 /|
   /                           / |
  /___________________________/  /
  |                           | /
  |___________________________|/
"""

        case 2:
            return """
  []    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
  []    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
  [][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
  []    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
  []    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

              ___________
              |         |
              |         |
              |         @
              |         |
              |         |
              |
              |
     _________|__________________
    /         |                 /|
   /                           / |
  /___________________________/  /
  |                           | /
  |___________________________|/
"""

        case 3:
            return """
  []    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
  []    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
  [][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
  []    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
  []    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

              ___________
              |         |
              |         |
              |         @
              |        /|
              |         |
              |
              |
     _________|__________________
    /         |                 /|
   /                           / |
  /___________________________/  /
  |                           | /
  |___________________________|/
"""

        case 4:
            return """
  []    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
  []    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
  [][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
  []    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
  []    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

              ___________
              |         |
              |         |
              |         @
              |        /|\\
              |         |
              |
              |
     _________|__________________
    /         |                 /|
   /                           / |
  /___________________________/  /
  |                           | /
  |___________________________|/
"""

        case 5:
            return """
  []    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
  []    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
  [][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
  []    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
  []    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

              ___________
              |         |
              |         |
              |         @
              |        /|\\
              |         |
              |        /
              |
     _________|__________________
    /         |                 /|
   /                           / |
  /___________________________/  /
  |                           | /
  |___________________________|/
"""

        case 6:
            return """
  []    []     []     []]    []   [][][][]   []]      [[]     []     []]   []
  []    []    [][]    [][]   []  []      []  [][]    [][]    [][]    [][]  []
  [][][][]   []  []   [] []  []  []          [] []  [] []   []  []   [] [] []
  []    []  [][][][]  []  [] []  []  []]][]  []  [][]  []  [][][][]  []  [][]
  []    []  []    []  []    [[]   [][[[]]]   []   []   []  []    []  []   [[]

              ___________
              |         |
              |         |
              |         @
              |        /|\\
              |         |
              |        / \\
              |
     _________|__________________
    /         |                 /|
   /                           / |
  /___________________________/  /
  |                           | /
  |___________________________|/
"""