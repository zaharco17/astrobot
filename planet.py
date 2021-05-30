import ephem
import datetime

a = "Mercury"

def planet(a):
    Pl = getattr(ephem,a)(datetime.date.today())
    constellation = ephem.constellation(Pl)
    return constellation

print (planet(a))
 




planets = 'Mercury, Venus, Earth, Mars, Jupiter, Saturn, Uranus, Neptune'
