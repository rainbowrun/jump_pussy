import random

genders = [
  'boy',
  'girl']

first_names = [
  'david',
  'elizabeth',
  'fiona',
  'george',
  'hector']

last_names = [
  'bell',
  'brown',
  'collins',
  'miller',
  'wilson']

start_times = [
  '5:00',
  '5:30',
  '6:00',
  '6:30',
  '7:00']

costumes = [
  'ghost',
  'witch',
  'athlete',
  'monster',
  'dog']

activities = [
  'trick-or-treating',
  'haunted hayrides',
  'pumpkin picking',
  'carving pumpkins',
  'bobbing for apples']

class Person:
  def __init__(self, gender, first_name, last_name,
               start_time, costume, activity):
    self.gender = gender
    self.first_name = first_name
    self.last_name = last_name
    self.start_time = start_time
    self.costume = costume
    self.activity = activity

    self.good = True

  def __str__(self):
    return f'{gender}:{first_name}:{last_name}:{start_time}:{costume}:{activity}'


persons = []

for gender in genders:
  for first_name in first_names:
    for last_name in last_names:
      for start_time in start_times:
        for costume in costumes:
          for activity in activities:
            persons.append(Person(gender, first_name, last_name,
                                  start_time, costume, activity))


def CountGoodPerson(persons):
   good = 0
   for person in persons:
     if person.good:
       good += 1

   print(f'There are possible {good} persons.')


def CheckRule(persons, rule):
  for person in persons:
    if person.good:
      rule(person)


def ListAllCombinations(all_persons):
  # Only save valid persons.
  persons = []
  for person in all_persons:
    if person.good:
      persons.append(person)

  assert len(persons) >= 5, f'Not enough person available {len(persons)}'
  print(f'There are {len(persons)} valid persons in all_persons.')

  for i, person in enumerate(persons):
    print(i, person)

  person_combinations = []

  for i1 in range(len(persons)):
    print(f'i1={i1}')
    for i2 in range(i1+1, len(persons)):
      for i3 in range(i2+1, len(persons)):
        for i4 in range(i3+1, len(persons)):
          for i5 in range(i4+1, len(persons)):
            # Check attributes uniques.

            if len(set([
                persons[i1].first_name,
                persons[i2].first_name,
                persons[i3].first_name,
                persons[i4].first_name,
                persons[i5].first_name])) != 5:
              continue

            if len(set([
                persons[i1].last_name,
                persons[i2].last_name,
                persons[i3].last_name,
                persons[i4].last_name,
                persons[i5].last_name])) != 5:
              continue

            if len(set([
                persons[i1].start_time,
                persons[i2].start_time,
                persons[i3].start_time,
                persons[i4].start_time,
                persons[i5].start_time])) != 5:
              continue

            if len(set([
                persons[i1].costume,
                persons[i2].costume,
                persons[i3].costume,
                persons[i4].costume,
                persons[i5].costume])) != 5:
              continue

            if len(set([
                persons[i1].activity,
                persons[i2].activity,
                persons[i3].activity,
                persons[i4].activity,
                persons[i5].activity])) != 5:
              continue

             Check if it has 3 boys and 2 girls.
            num_boys = 0
            num_girls = 0
            for i in [i1, i2, i3, i4, i5]:
              if person[i].gender == 'boy':
                num_boys += 1
              else:
                num_girls += 1
            if num_boys != 3 or num_girls != 2:
              continue

            person_combinations.append([
                persons[i1],
                persons[i2],
                persons[i3],
                persons[i4],
                persons[i5],
                ])

  print(f'There are {len(person_combinations)} combinations.')


def rule_name_1(person):
  if person.first_name == 'david':
    if person.gender == 'boy':
      person.good = True
    else:
      person.good = False

def rule_name_2 (person):
  if person.first_name=='george':
    if person.gender=='boy':
      person.good=True
    else:
      person.good=False

def rule_name_3 (person):
  if person.first_name=='hector':
    if person.gender=='boy':
      person.good=True
    else:
      person.good=False

def rule_name_4 (person):
  if person.first_name=='fiona':
    if person.gender=='girl':
      person.good=True
    else:
      person.good=False

def rule_name_5 (person):
  if person.first_name=='elizabeth':
    if person.gender=='girl':
      person.good=True
    else:
      person.good=False


def rule_1(person):
  if person.costume == 'ghost':
    if person.start_time == '5:30':
      if person.activity == 'trick-or-treating':
        person.good = True
      else:
        person.good = False
    else:
      person.good = False
  else:
    if person.start_time == '5:30' or person.activity == 'trick-or-treating':
        person.good = False


def rule_2(person):
  if person.gender == 'girl':
    if person.costume == 'witch':
       if person.activity == 'pumpkin picking':
         person.good = True
       else:
         person.good = False
  else:
    if person.costume == 'witch' or person.activity == 'pumpkin picking':
      person.good = False


def rule_3(person):
  if person.first_name == 'hector':
    if person.start_time != '7:00' or person.activity != 'trick-or-treating':
      person.good = False
    else:
      person.good = True
  else:
    if person.start_time == '7:00' or person.activity == 'trick-or-treating':
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


def rule_10(person):
  if person.last_name == 'brown':
    if person.gender == 'girl':
      person.good = False
      return

    if (person.activity == 'carving pumpkins' or
        person.activity == 'bobbing apples'):
      person.good = False



CountGoodPerson(persons)
CheckRule(persons, rule_name_1)
CountGoodPerson(persons)
CheckRule(persons, rule_name_2)
CountGoodPerson(persons)
CheckRule(persons, rule_name_3)
CountGoodPerson(persons)
CheckRule(persons, rule_name_4)
CountGoodPerson(persons)
CheckRule(persons, rule_name_5)
CountGoodPerson(persons)

CheckRule(persons, rule_1)
CountGoodPerson(persons)
CheckRule(persons, rule_2)
CountGoodPerson(persons)
CheckRule(persons, rule_3)
CountGoodPerson(persons)
CheckRule(persons, rule_4)
CountGoodPerson(persons)
CheckRule(persons, rule_6)
CountGoodPerson(persons)
CheckRule(persons, rule_7)
CountGoodPerson(persons)
CheckRule(persons, rule_8)
CountGoodPerson(persons)
CheckRule(persons, rule_10)
CountGoodPerson(persons)

ListAllCombinations(persons)
