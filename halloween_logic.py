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
    return (f'{self.gender}:{self.first_name}:{self.last_name}:'
            f'{self.start_time}:{self.costume}:{self.activity}')


def CountGoodPerson(persons):
   good_persons = [person for person in persons if person.good]
   print(f'There are possible {len(good_persons)} persons. Here are some of them:')
   for choice in random.choices(good_persons, k=10):
     print('\t', choice)


def CheckRule(persons, rule):
  for person in persons:
    if person.good:
      rule(person)


def ListAllCombinations(persons):
  good_persons = [person for person in persons if person.good]

  assert len(good_persons) >= 5, f'Not enough person available {len(good_persons)}'
  print(f'There are {len(good_persons)} good persons in all {len(persons)} persons.')

  for i, person in enumerate(good_persons):
    print('\t', i, person)

  person_combinations = []

  for i1 in range(len(good_persons)):
    print(f'i1={i1}')
    for i2 in range(i1+1, len(good_persons)):
      for i3 in range(i2+1, len(good_persons)):
        for i4 in range(i3+1, len(good_persons)):
          for i5 in range(i4+1, len(good_persons)):
            # Check attributes uniques.

            if len(set([
                good_persons[i1].first_name,
                good_persons[i2].first_name,
                good_persons[i3].first_name,
                good_persons[i4].first_name,
                good_persons[i5].first_name])) != 5:
              continue

            if len(set([
                good_persons[i1].last_name,
                good_persons[i2].last_name,
                good_persons[i3].last_name,
                good_persons[i4].last_name,
                good_persons[i5].last_name])) != 5:
              continue

            if len(set([
                good_persons[i1].start_time,
                good_persons[i2].start_time,
                good_persons[i3].start_time,
                good_persons[i4].start_time,
                good_persons[i5].start_time])) != 5:
              continue

            if len(set([
                good_persons[i1].costume,
                good_persons[i2].costume,
                good_persons[i3].costume,
                good_persons[i4].costume,
                good_persons[i5].costume])) != 5:
              continue

            if len(set([
                good_persons[i1].activity,
                good_persons[i2].activity,
                good_persons[i3].activity,
                good_persons[i4].activity,
                good_persons[i5].activity])) != 5:
              continue

            # Check if it has 3 boys and 2 girls.
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
                good_persons[i1],
                good_persons[i2],
                good_persons[i3],
                good_persons[i4],
                good_persons[i5],
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


def main():
  persons = []

  for gender in genders:
    for first_name in first_names:
      for last_name in last_names:
        for start_time in start_times:
          for costume in costumes:
            for activity in activities:
              persons.append(Person(gender, first_name, last_name,
                                    start_time, costume, activity))


  CountGoodPerson(persons)

  for rule in [rule_name_1, rule_name_2, rule_name_3, rule_name_4, rule_name_5,
               rule_1, rule_2, rule_3, rule_4, rule_6, rule_7, rule_8, rule_10,
              ]:
    CheckRule(persons, rule)
    CountGoodPerson(persons)

  ListAllCombinations(persons)


if __name__ == '__main__':
  main()
