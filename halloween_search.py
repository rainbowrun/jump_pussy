import sys

class Person:
  def __init__(self, gender, first_name, last_name,
               start_time, costume, activity):
    self.gender = gender
    self.first_name = first_name
    self.last_name = last_name
    self.start_time = start_time
    self.costume = costume
    self.activity = activity

    # Flag to indicate whether this attribute combination is good.
    self.good = True

  def __str__(self):
    return (f'{self.gender}:{self.first_name}:{self.last_name}:'
            f'{self.start_time}:{self.costume}:{self.activity}')


def rule_name(person):
  if person.first_name == 'david':
    if person.gender == 'boy':
      person.good = True
    else:
      person.good = False

  if person.first_name=='george':
    if person.gender=='boy':
      person.good=True
    else:
      person.good=False

  if person.first_name=='hector':
    if person.gender=='boy':
      person.good=True
    else:
      person.good=False

  if person.first_name=='fiona':
    if person.gender=='girl':
      person.good=True
    else:
      person.good=False

  if person.first_name=='elizabeth':
    if person.gender=='girl':
      person.good=True
    else:
      person.good=False


def rule_1(person):
  if person.costume == 'ghost':
    if person.start_time == '5:00':
      person.good = True
    else:
      person.good = False
  else:
    if person.start_time == '5:00':
        person.good = False


def rule_2(person):
  if person.gender == 'girl':
    if person.costume == 'witch':
       if person.activity == 'pumpkin picking':
         person.good = True
       else:
         person.good = False
  else:
    if (person.costume == 'witch' or
        person.activity == 'pumpkin picking'):
      person.good = False


def rule_3(person):
  if person.first_name == 'hector':
    if (person.start_time != '7:00' or 
        person.activity != 'trick-or-treating'):
      person.good = False
    else:
      person.good = True
  else:
    if (person.start_time == '7:00' or
        person.activity == 'trick-or-treating'):
      person.good = False
    else:
      person.good = True


def rule_4(person):
  if person.last_name == 'bell':
    if person.gender == 'boy':
      person.good = False
      return

    if person.costume == 'ghost' or person.costume == 'monster':
      person.good = False
      return
 

def is_time1_30_minutes_late_than_time2(time1, time2):
  if time1 == '5:00':
    return False
  
  if time1 == '5:30':
    return time2 == '5:00'

  if time1 == '6:00':
    return time2 == '5:30'
  
  if time1 == '6:30':
    return time2 == '6:00'

  if time1 == '7:00':
    return time2 == '6:30'

  assert False, f'Should not get here. {time1}, {time2}'
  

def rule_6(person):
  if person.last_name == 'wilson':
    if person.gender == 'girl':
      person.good = False
      return

    if person.costume == 'ghost' or person.costume == 'monster':
      person.good = False
      return


def rule_7(person):
  if person.first_name=="fiona":
    if person.start_time=='6:00':
      person.good = True
    else:
      person.good = False
  else:
    if person.start_time == '6:00':
      person.good = False


def rule_8(person):
  if person.last_name == 'miller':
    if person.gender == 'boy':
      person.good = False
      return

    if person.costume != 'dog' or person.start_time != '5:30':
      person.good = False
      return

    if person.activity == 'carving pumpkins':
      person.good = False
      return

  else:
    if person.costume == 'dog' or person.start_time == '5:30':
      person.good = False


def rule_5(combination):
  david = None

  for person in combination:
    if person.first_name == 'david':
      if (person.last_name == 'collins' or
          person.last_name == 'wilson'):
        return False
      david = person
      break

  if not david:
    return True

  fiona = None
  for person in combination:
    if person.first_name == 'fiona':
      fiona = person
      break
  if not fiona:
    return True

  return is_time1_30_minutes_late_than_time2(
      david.start_time, fiona.start_time)


# Return -1 if time1 < time2
# 0 if they equal
# 1 if time1 > time2
def compare_time(time1, time2):
  fields = time1.split(':')
  hour1 = int(fields[0])
  minute1 = int(fields[1])

  fields = time2.split(':')
  hour2 = int(fields[0])
  minute2 = int(fields[1])

  if hour2 > hour1:
     return -1
  elif hour1 > hour2:
     return 1
  elif minute2 > minute1:
     return -1
  elif minute1 > minute2:
     return 1
  else:
     return 0


def rule_9(combination):
  monster_boy = None
  for person in combination:
    if person.gender == 'boy' and person.costume == 'monster':
      monster_boy = person
      break

  if not monster_boy:
    return True

  athlete_boy = None
  for person in combination:
    if person.gender == 'boy' and person.costume == 'athlete':
      athlete_boy = person
      break

  if not athlete_boy:
    return True

  result = compare_time(monster_boy.start_time, athlete_boy.start_time)
  if result == -1:
    return True
  else:
    return False


def rule_10(person):
  if person.last_name == 'brown':
    if person.gender == 'girl':
      person.good = False
      return

    if (person.activity == 'carving pumpkins' or
        person.activity == 'bobbing apples'):
      person.good = False


GENDERS = set([
  'boy',
  'girl'])

FIRST_NAMES = set([
  'david',
  'elizabeth',
  'fiona',
  'george',
  'hector'])

LAST_NAMES = set([
  'bell',
  'brown',
  'collins',
  'miller',
  'wilson'])

START_TIMES = set([
  '5:00',
  '5:30',
  '6:00',
  '6:30',
  '7:00'])

COSTUMES = set([
  'ghost',
  'witch',
  'athlete',
  'monster',
  'dog'])

ACTIVITIES = set([
  'trick-or-treating',
  'haunted hayrides',
  'pumpkin picking',
  'carving pumpkins',
  'bobbing for apples'])


class PersonGenerator:
  def __init__(self, existing_persons):
    self.available_genders = GENDERS
    self.available_first_names = FIRST_NAMES - set(
        [p.first_name for p in existing_persons])
    self.available_last_names = LAST_NAMES - set(
        [p.last_name for p in existing_persons])
    self.available_start_times = START_TIMES - set(
        [p.start_time for p in existing_persons])
    self.available_costumes = COSTUMES - set(
        [p.costume for p in existing_persons])
    self.available_activities = ACTIVITIES - set(
        [p.activity for p in existing_persons])

  def NextPossiblePerson(self):
    for gender in self.available_genders:
      for first_name in self.available_first_names:
        for last_name in self.available_last_names:
          for start_time in self.available_start_times:
            for costume in self.available_costumes:
              for activity in self.available_activities:
                person = Person(gender, first_name, last_name,
                                start_time, costume, activity)

                # Check if the person is good.
                for rule in [rule_name, rule_1, rule_2, rule_3, rule_4,
                             rule_6, rule_7, rule_8, rule_10]:
                  
                  rule(person)
                  if not person.good: break

                if not person.good: continue

                yield person


def AddOnePerson(persons):
  person_generator = PersonGenerator(persons)
  for next_person in person_generator.NextPossiblePerson():
    persons.append(next_person)

    if not rule_5(persons):
      del persons[-1]
      continue

    if not rule_9(persons):
      del persons[-1]
      continue

    if len(persons) < 5:
      AddOnePerson(persons)

    num_boys = 0
    num_girls = 0
    for person in persons:
      if person.gender == 'boy':
        num_boys += 1
      else:
        num_girls += 1
    if num_boys != 3 or num_girls != 2:
      del persons[-1]
      continue

    for person in persons:
      print(person)
    sys.exit(0)


def main():
  persons = []
  AddOnePerson(persons)


if __name__ == '__main__':
  main()
