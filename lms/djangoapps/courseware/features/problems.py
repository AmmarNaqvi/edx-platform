from lettuce import world, step
from lettuce.django import django_url
from selenium.webdriver.support.ui import Select
from common import i_am_registered_for_the_course

problem_urls = { 'drop down': '/courses/edX/model_course/2013_Spring/courseware/Problem_Components/Drop_Down_Problems',
                'multiple choice': '/courses/edX/model_course/2013_Spring/courseware/Problem_Components/Multiple_Choice_Problems',
                'checkbox': '/courses/edX/model_course/2013_Spring/courseware/Problem_Components/Checkbox_Problems', }

@step(u'I am viewing a "([^"]*)" problem')
def view_problem(step, problem_type):
    i_am_registered_for_the_course(step, 'edX/model_course/2013_Spring')
    url = django_url(problem_urls[problem_type])
    world.browser.visit(url)

@step(u'I answer a "([^"]*)" problem "([^"]*)ly"')
def answer_problem(step, problem_type, correctness):
    assert(correctness in ['correct', 'incorrect'])

    if problem_type == "drop down":
        select_name = "input_i4x-edX-model_course-problem-Drop_Down_Problem_2_1"
        option_text = 'Option 2' if correctness == 'correct' else 'Option 3'
        world.browser.select(select_name, option_text)

    elif problem_type == "multiple choice":
        if correctness == 'correct':
            world.browser.find_by_css("#input_i4x-edX-model_course-problem-Multiple_Choice_Problem_2_1_choice_choice_3").check()
        else:
            world.browser.find_by_css("#input_i4x-edX-model_course-problem-Multiple_Choice_Problem_2_1_choice_choice_2").check()

    elif problem_type == "checkbox":
        if correctness == 'correct':
            world.browser.find_by_css('#input_i4x-edX-model_course-problem-Checkbox_Problem_2_1_choice_0').check()
            world.browser.find_by_css('#input_i4x-edX-model_course-problem-Checkbox_Problem_2_1_choice_2').check()
        else:
            world.browser.find_by_css('#input_i4x-edX-model_course-problem-Checkbox_Problem_2_1_choice_3').check()

    check_problem(step)

@step(u'I check a problem')
def check_problem(step):
    world.browser.find_by_css("input.check").click()

@step(u'I reset the problem')
def reset_problem(step):
    world.browser.find_by_css('input.reset').click()

@step(u'My "([^"]*)" answer is marked "([^"]*)"')
def assert_answer_mark(step, problem_type, correctness):
    assert(correctness in ['correct', 'incorrect', 'unanswered'])

    if problem_type == "multiple choice":
        if correctness == 'unanswered':
            mark_classes = ['.choicegroup_correct', '.choicegroup_incorrect',
                            '.correct', '.incorrect']
            for css in mark_classes:
                assert(world.browser.is_element_not_present_by_css(css))
                    
        else:
            if correctness == 'correct':
                mark_class = '.choicegroup_correct'
                assert(world.browser.is_element_present_by_css(mark_class, wait_time=4))

            else:
                # Two ways to be marked incorrect: either applying a 
                # class to the label (marking a particular option)
                # or applying a class to a span (marking the whole problem incorrect)
                mark_classes = ['.choicegroup_incorrect', '.incorrect']
                assert(world.browser.is_element_present_by_css(mark_classes[0], wait_time=4) or
                        world.browser.is_element_present_by_css(mark_classes[1], wait_time=4))

    else:
        if correctness == 'unanswered':
            assert(world.browser.is_element_not_present_by_css('.correct'))
            assert(world.browser.is_element_not_present_by_css('.incorrect'))

        else:
            mark_class = '.correct' if correctness == 'correct' else '.incorrect'
            assert(world.browser.is_element_present_by_css(mark_class, wait_time=4))
