#!/usr/bin/env python3
"""
Python function that changes all topics of a school document based
on the name
- Prototype: def update_topics(mongo_collection, name, topics):
- mongo_collection will be the pymongo collection object
- name (string) will be the school name to update
- topics (list of strings) will be the list of topics approached in
the school
"""


def top_students(mongo_collection):
    """
    Python function that changes all topics of a school document
    based on the name
    - name (string) will be the school name to update
    - topics (list of strings) will be the list of topics approached
    in the school
    """
    students = list(mongo_collection.find())

    for student in students:
        total_score = sum(topic['score'] for topic in student['topics'])
        average_score = total_score / len(student['topics'])
        student['averageScore'] = round(average_score, 2)

    sorted_students = sorted(students,
                             key=lambda x: x['averageScore'],
                             reverse=True)
    return sorted_students
