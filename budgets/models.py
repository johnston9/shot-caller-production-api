"""
Models for Budgets App
"""
from django.db import models
from django.contrib.auth.models import User


class Budget(models.Model):
    """
    Budget model
    """
    project = models.CharField(max_length=25, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    above_the_line_total = models.CharField(max_length=25, blank=True)
    below_the_lineB_total = models.CharField(max_length=25, blank=True)
    grand_total = models.CharField(max_length=25, blank=True)
    title = models.CharField(max_length=25, blank=True)
    series = models.CharField(max_length=25, blank=True)
    prodco = models.CharField(max_length=25, blank=True)
    format = models.CharField(max_length=25, blank=True)
    location = models.CharField(max_length=25, blank=True)
    dated = models.CharField(max_length=25, blank=True)
    writer = models.CharField(max_length=25, blank=True)
    prelimfin = models.CharField(max_length=25, blank=True)
    preparedby = models.CharField(max_length=25, blank=True)
    approvedby = models.CharField(max_length=25, blank=True)
    approvedbyco = models.CharField(max_length=25, blank=True)
    research = models.CharField(max_length=25, blank=True)
    prep = models.CharField(max_length=25, blank=True)
    shoot = models.CharField(max_length=25, blank=True)
    wrap = models.CharField(max_length=25, blank=True)
    post = models.CharField(max_length=25, blank=True)
    length_total = models.CharField(max_length=25, blank=True)
    story_rights = models.CharField(max_length=25, blank=True)
    miscellaneous = models.CharField(max_length=25, blank=True)
    rights_total = models.CharField(max_length=25, blank=True)
    research_development = models.CharField(max_length=25, blank=True)
    prelim_budget = models.CharField(max_length=25, blank=True)
    consultant_expenses = models.CharField(max_length=25, blank=True)
    office_expenses = models.CharField(max_length=25, blank=True)
    staff = models.CharField(max_length=25, blank=True)
    travel_expenses_development = models.CharField(max_length=25, blank=True)
    living_expenses_development = models.CharField(max_length=25, blank=True)
    other_development = models.CharField(max_length=25, blank=True)
    development_total = models.CharField(max_length=25, blank=True)
    writers_quantity = models.CharField(max_length=25, blank=True)
    writers_units_number = models.CharField(max_length=25, blank=True)
    writers_units_name = models.CharField(max_length=25, blank=True)
    writers_rate = models.CharField(max_length=25, blank=True)
    writers_total = models.CharField(max_length=25, blank=True)
    consultants_quantity = models.CharField(max_length=25, blank=True)
    consultants_units_number = models.CharField(max_length=25, blank=True)
    consultants_units_name = models.CharField(max_length=25, blank=True)
    consultants_rate = models.CharField(max_length=25, blank=True)
    consultants_total = models.CharField(max_length=25, blank=True)
    editors_scenario_quantity = models.CharField(max_length=25, blank=True)
    editors_scenario_units_number = models.CharField(max_length=25, blank=True)
    editors_scenario_units_name = models.CharField(max_length=25, blank=True)
    editors_scenario_rate = models.CharField(max_length=25, blank=True)
    editors_scenario_total = models.CharField(max_length=25, blank=True)
    admin_scenario_quantity = models.CharField(max_length=25, blank=True)
    admin_scenario_units_number = models.CharField(max_length=25, blank=True)
    admin_scenario_units_name = models.CharField(max_length=25, blank=True)
    admin_scenario_rate = models.CharField(max_length=25, blank=True)
    admin_scenario_total = models.CharField(max_length=25, blank=True)
    office_expenses_scenario = models.CharField(max_length=25, blank=True)
    travel_expenses_scenario = models.CharField(max_length=25, blank=True)
    living_expenses_scenario = models.CharField(max_length=25, blank=True)
    other_scenario = models.CharField(max_length=25, blank=True)
    scenario_total = models.CharField(max_length=25, blank=True)
    executive_producers_quantity = models.CharField(max_length=25, blank=True)
    producers_quantity = models.CharField(max_length=25, blank=True)
    line_producers_quantity = models.CharField(max_length=25, blank=True)
    co_producers_quantity = models.CharField(max_length=25, blank=True)
    associate_producers_quantity = models.CharField(max_length=25, blank=True)
    directors_quantity = models.CharField(max_length=25, blank=True)
    unit2_directors_quantity = models.CharField(max_length=25, blank=True)
    executive_producers_rate = models.CharField(max_length=25, blank=True)
    producers_rate = models.CharField(max_length=25, blank=True)
    line_producers_rate = models.CharField(max_length=25, blank=True)
    co_producers_rate = models.CharField(max_length=25, blank=True)
    associate_producers_rate = models.CharField(max_length=25, blank=True)
    directors_rate = models.CharField(max_length=25, blank=True)
    unit2_directors_rate = models.CharField(max_length=25, blank=True)
    executive_producers_total = models.CharField(max_length=25, blank=True)
    producers_total = models.CharField(max_length=25, blank=True)
    line_producers_total = models.CharField(max_length=25, blank=True)
    co_producers_total = models.CharField(max_length=25, blank=True)
    associate_producers_total = models.CharField(max_length=25, blank=True)
    directors_total = models.CharField(max_length=25, blank=True)
    unit2_directors_total = models.CharField(max_length=25, blank=True)
    travel_expenses_producers_dirs = models.CharField(
        max_length=25, blank=True)
    living_expenses_producers_dirs = models.CharField(
        max_length=25, blank=True)
    other_producers_dirs = models.CharField(max_length=25, blank=True)
    fringes_taxes_producers_dirs = models.CharField(max_length=25, blank=True)
    producers_dirs_total = models.CharField(max_length=25, blank=True)
    stars = models.CharField(max_length=25, blank=True)
    stars_rights_payments = models.CharField(max_length=25, blank=True)
    travel_expenses_stars = models.CharField(max_length=25, blank=True)
    living_expenses_stars = models.CharField(max_length=25, blank=True)
    other_stars = models.CharField(max_length=25, blank=True)
    fringes_taxes_stars = models.CharField(max_length=25, blank=True)
    music = models.CharField(max_length=25, blank=True)
    music_supervisor = models.CharField(max_length=25, blank=True)
    travel_expenses_music = models.CharField(max_length=25, blank=True)
    living_expenses_music = models.CharField(max_length=25, blank=True)
    music_rights_addl_songs = models.CharField(max_length=25, blank=True)
    other_music = models.CharField(max_length=25, blank=True)
    fringes_taxes_music = models.CharField(max_length=25, blank=True)
    stars_music_total = models.CharField(max_length=25, blank=True)
    principals_quantity = models.CharField(max_length=25, blank=True)
    principals_units_number = models.CharField(max_length=25, blank=True)
    principals_units_name = models.CharField(max_length=25, blank=True)
    principals_rate = models.CharField(max_length=25, blank=True)
    actors_quantity = models.CharField(max_length=25, blank=True)
    actors_units_number = models.CharField(max_length=25, blank=True)
    actors_units_name = models.CharField(max_length=25, blank=True)
    actors_rate = models.CharField(max_length=25, blank=True)
    stuntcoordinators_quantity = models.CharField(max_length=25, blank=True)
    stuntcoordinators_units_number = models.CharField(
        max_length=25, blank=True)
    stuntcoordinators_units_name = models.CharField(max_length=25, blank=True)
    stuntcoordinators_rate = models.CharField(max_length=25, blank=True)
    stuntperformers_quantity = models.CharField(max_length=25, blank=True)
    stuntperformers_units_number = models.CharField(max_length=25, blank=True)
    stuntperformers_units_name = models.CharField(max_length=25, blank=True)
    stuntperformers_rate = models.CharField(max_length=25, blank=True)
    otherperformers_quantity = models.CharField(max_length=25, blank=True)
    otherperformers_units_number = models.CharField(max_length=25, blank=True)
    otherperformers_units_name = models.CharField(max_length=25, blank=True)
    otherperformers_rate = models.CharField(max_length=25, blank=True)
    extras_quantity = models.CharField(max_length=25, blank=True)
    extras_units_number = models.CharField(max_length=25, blank=True)
    extras_units_name = models.CharField(max_length=25, blank=True)
    extras_rate = models.CharField(max_length=25, blank=True)
    principals_total = models.CharField(max_length=25, blank=True)
    actors_total = models.CharField(max_length=25, blank=True)
    stuntcoordinators_total = models.CharField(max_length=25, blank=True)
    stuntperformers_total = models.CharField(max_length=25, blank=True)
    otherperformers_total = models.CharField(max_length=25, blank=True)
    extras_total = models.CharField(max_length=25, blank=True)
    casting_director = models.CharField(max_length=25, blank=True)
    extras_casting = models.CharField(max_length=25, blank=True)
    other_cast = models.CharField(max_length=25, blank=True)
    fringes_taxes_cast = models.CharField(max_length=25, blank=True)
    rights_payments_cast = models.CharField(max_length=25, blank=True)
    cast_total = models.CharField(max_length=25, blank=True)
    production_manager_quantity = models.CharField(max_length=25, blank=True)
    production_manager_units_number = models.CharField(
        max_length=25, blank=True)
    production_manager_units_name = models.CharField(max_length=25, blank=True)
    production_manager_rate = models.CharField(max_length=25, blank=True)
    production_supervisor_quantity = models.CharField(
        max_length=25, blank=True)
    production_supervisor_units_number = models.CharField(
        max_length=25, blank=True)
    production_supervisor_units_name = models.CharField(
        max_length=25, blank=True)
    production_supervisor_rate = models.CharField(max_length=25, blank=True)
    production_coordinator_quantity = models.CharField(
        max_length=25, blank=True)
    production_coordinator_units_number = models.CharField(
        max_length=25, blank=True)
    production_coordinator_units_name = models.CharField(
        max_length=25, blank=True)
    production_coordinator_rate = models.CharField(max_length=25, blank=True)
    unit_manager_quantity = models.CharField(max_length=25, blank=True)
    unit_manager_units_number = models.CharField(max_length=25, blank=True)
    unit_manager_units_name = models.CharField(max_length=25, blank=True)
    unit_manager_rate = models.CharField(max_length=25, blank=True)
    location_manager_quantity = models.CharField(max_length=25, blank=True)
    location_manager_units_number = models.CharField(max_length=25, blank=True)
    location_manager_units_name = models.CharField(max_length=25, blank=True)
    location_manager_rate = models.CharField(max_length=25, blank=True)
    location_manager_assistant_quantity = models.CharField(
        max_length=25, blank=True)
    location_manager_assistant_units_number = models.CharField(
        max_length=25, blank=True)
    location_manager_assistant_units_name = models.CharField(
        max_length=25, blank=True)
    location_manager_assistant_rate = models.CharField(
        max_length=25, blank=True)
    production_assistants_quantity = models.CharField(
        max_length=25, blank=True)
    production_assistants_units_number = models.CharField(
        max_length=25, blank=True)
    production_assistants_units_name = models.CharField(
        max_length=25, blank=True)
    production_assistants_rate = models.CharField(max_length=25, blank=True)
    production_secretary_quantity = models.CharField(max_length=25, blank=True)
    production_secretary_units_number = models.CharField(
        max_length=25, blank=True)
    production_secretary_units_name = models.CharField(
        max_length=25, blank=True)
    production_secretary_rate = models.CharField(max_length=25, blank=True)
    production_accountant_quantity = models.CharField(
        max_length=25, blank=True)
    production_accountant_units_number = models.CharField(
        max_length=25, blank=True)
    production_accountant_units_name = models.CharField(
        max_length=25, blank=True)
    production_accountant_rate = models.CharField(max_length=25, blank=True)
    production_accountant_assistant_quantity = models.CharField(
        max_length=25, blank=True)
    production_accountant_assistant_units_number = models.CharField(
        max_length=25, blank=True)
    production_accountant_assistant_units_name = models.CharField(
        max_length=25, blank=True)
    production_accountant_assistant_rate = models.CharField(
        max_length=25, blank=True)
    scriptsupervisor_continuity_quantity = models.CharField(
        max_length=25, blank=True)
    scriptsupervisor_continuity_units_number = models.CharField(
        max_length=25, blank=True)
    scriptsupervisor_continuity_units_name = models.CharField(
        max_length=25, blank=True)
    scriptsupervisor_continuity_rate = models.CharField(
        max_length=25, blank=True)
    payroll_quantity = models.CharField(max_length=25, blank=True)
    payroll_units_number = models.CharField(max_length=25, blank=True)
    payroll_units_name = models.CharField(max_length=25, blank=True)
    payroll_rate = models.CharField(max_length=25, blank=True)
    other_production_quantity = models.CharField(max_length=25, blank=True)
    other_production_units_number = models.CharField(max_length=25, blank=True)
    other_production_units_name = models.CharField(max_length=25, blank=True)
    other_production_rate = models.CharField(max_length=25, blank=True)
    directors_assistant_quantity = models.CharField(max_length=25, blank=True)
    directors_assistant_units_number = models.CharField(
        max_length=25, blank=True)
    directors_assistant_units_name = models.CharField(
        max_length=25, blank=True)
    directors_assistant_rate = models.CharField(max_length=25, blank=True)
    assistant_director_1st_quantity = models.CharField(
        max_length=25, blank=True)
    assistant_director_1st_units_number = models.CharField(
        max_length=25, blank=True)
    assistant_director_1st_units_name = models.CharField(
        max_length=25, blank=True)
    assistant_director_1st_rate = models.CharField(max_length=25, blank=True)
    assistant_director_2nd_quantity = models.CharField(
        max_length=25, blank=True)
    assistant_director_2nd_units_number = models.CharField(
        max_length=25, blank=True)
    assistant_director_2nd_units_name = models.CharField(
        max_length=25, blank=True)
    assistant_director_2nd_rate = models.CharField(max_length=25, blank=True)
    assistant_director_3rd_quantity = models.CharField(
        max_length=25, blank=True)
    assistant_director_3rd_units_number = models.CharField(
        max_length=25, blank=True)
    assistant_director_3rd_units_name = models.CharField(
        max_length=25, blank=True)
    assistant_director_3rd_rate = models.CharField(max_length=25, blank=True)
    craft_services_quantity = models.CharField(max_length=25, blank=True)
    craft_services_units_number = models.CharField(max_length=25, blank=True)
    craft_services_units_name = models.CharField(max_length=25, blank=True)
    craft_services_rate = models.CharField(max_length=25, blank=True)
    productionmanager_total = models.CharField(max_length=25, blank=True)
    productionsupervisor_total = models.CharField(max_length=25, blank=True)
    productioncoordinator_total = models.CharField(max_length=25, blank=True)
    unitmanager_total = models.CharField(max_length=25, blank=True)
    locationmanager_total = models.CharField(max_length=25, blank=True)
    locationmanagerassistant_total = models.CharField(
        max_length=25, blank=True)
    productionassistants_total = models.CharField(max_length=25, blank=True)
    productionsecretary_total = models.CharField(max_length=25, blank=True)
    productionaccountant_total = models.CharField(max_length=25, blank=True)
    productionaccountantassistant_total = models.CharField(
        max_length=25, blank=True)
    scriptsupervisorcontinuity_total = models.CharField(
        max_length=25, blank=True)
    payroll_total = models.CharField(max_length=25, blank=True)
    otherproduction_total = models.CharField(max_length=25, blank=True)
    directorsassistant_total = models.CharField(max_length=25, blank=True)
    assistantdirector1st_total = models.CharField(max_length=25, blank=True)
    assistantdirector2nd_total = models.CharField(max_length=25, blank=True)
    assistantdirector3rd_total = models.CharField(max_length=25, blank=True)
    craftservices_total = models.CharField(max_length=25, blank=True)
    productionstaff_total = models.CharField(max_length=25, blank=True)

    class Meta:
        """ Meta for ordering """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} "
