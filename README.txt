This is basically a client to work with Jenkins

  from ci.jenkins import MrHat()
  m = MrHat()
  m.find_next_build('head')
