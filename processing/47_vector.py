from miniworlds import *
world = World()

@world.register
def act(self):
    m_vec = Vector(world.mouse.x(), world.mouse.y())
    center = Vector(200, 200)
    m_vec = m_vec - center
    print(m_vec.x, m_vec.y)
    m_vec.normalize()
    m_vec.multiply(100)
    m_vec.add(center)
    #print((m_vec.x, m_vec.y), (center.x, center.y))
    Line((center.x, center.y),(m_vec.x,m_vec.y))
    
world.run()