"""
Models for Budgets App
"""
from django.db import models
from django.contrib.auth.models import User


class Budget3(models.Model):
    """
    Budget3 model
    """
    project = models.CharField(max_length=25, blank=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    title = models.CharField(max_length=25, blank=True)
    office_rentals = models.CharField(max_length=25, blank=True)
    office_equipment = models.CharField(max_length=25, blank=True)
    office_supplies = models.CharField(max_length=25, blank=True)
    phones_net = models.CharField(max_length=25, blank=True)
    courier_postage = models.CharField(max_length=25, blank=True)
    office_other = models.CharField(max_length=25, blank=True)
    proOff_total = models.CharField(max_length=25, blank=True)
    studio_rentals = models.CharField(max_length=25, blank=True)
    power = models.CharField(max_length=25, blank=True)
    carpentry_rentals = models.CharField(max_length=25, blank=True)
    studio_fx_equipment = models.CharField(max_length=25, blank=True)
    studio_security = models.CharField(max_length=25, blank=True)
    studio_other = models.CharField(max_length=25, blank=True)
    studio_total = models.CharField(max_length=25, blank=True)
    surveying_scouting = models.CharField(max_length=25, blank=True)
    site_rentals = models.CharField(max_length=25, blank=True)
    site_power = models.CharField(max_length=25, blank=True)
    site_access = models.CharField(max_length=25, blank=True)
    site_insurance = models.CharField(max_length=25, blank=True)
    repairs_construction = models.CharField(max_length=25, blank=True)
    site_security = models.CharField(max_length=25, blank=True)
    site_other = models.CharField(max_length=25, blank=True)
    police_control = models.CharField(max_length=25, blank=True)
    site_total = models.CharField(max_length=25, blank=True)
    catering = models.CharField(max_length=25, blank=True)
    craft_expenses = models.CharField(max_length=25, blank=True)
    meal_penalty = models.CharField(max_length=25, blank=True)
    green_room = models.CharField(max_length=25, blank=True)
    first_aid = models.CharField(max_length=25, blank=True)
    outfitting = models.CharField(max_length=25, blank=True)
    medical_insurance = models.CharField(max_length=25, blank=True)
    unit_other = models.CharField(max_length=25, blank=True)
    unit_total = models.CharField(max_length=25, blank=True)
    fares = models.CharField(max_length=25, blank=True)
    accomatation_hotels = models.CharField(max_length=25, blank=True)
    per_diems = models.CharField(max_length=25, blank=True)
    taxis_limos = models.CharField(max_length=25, blank=True)
    shipping = models.CharField(max_length=25, blank=True)
    customs_brokerage = models.CharField(max_length=25, blank=True)
    other_trav_liv = models.CharField(max_length=25, blank=True)
    traliv_total = models.CharField(max_length=25, blank=True)
    production_cars = models.CharField(max_length=25, blank=True)
    trucks_vans = models.CharField(max_length=25, blank=True)
    buses = models.CharField(max_length=25, blank=True)
    motorhomes = models.CharField(max_length=25, blank=True)
    talent_cars = models.CharField(max_length=25, blank=True)
    support_vehicles = models.CharField(max_length=25, blank=True)
    boats_planes = models.CharField(max_length=25, blank=True)
    fuel = models.CharField(max_length=25, blank=True)
    repairs = models.CharField(max_length=25, blank=True)
    taxis = models.CharField(max_length=25, blank=True)
    parking = models.CharField(max_length=25, blank=True)
    licenses_permits = models.CharField(max_length=25, blank=True)
    brokerage_insurance = models.CharField(max_length=25, blank=True)
    other_transport = models.CharField(max_length=25, blank=True)
    transport_total = models.CharField(max_length=25, blank=True)
    rentals_carpentry = models.CharField(max_length=25, blank=True)
    carpentry_purchases = models.CharField(max_length=25, blank=True)
    painting_rentals = models.CharField(max_length=25, blank=True)
    painting_purchases = models.CharField(max_length=25, blank=True)
    backdrops_murals = models.CharField(max_length=25, blank=True)
    scaffolding = models.CharField(max_length=25, blank=True)
    warehouse_rental = models.CharField(max_length=25, blank=True)
    construction_other = models.CharField(max_length=25, blank=True)
    constructionmat_total = models.CharField(max_length=25, blank=True)
    drawing_supplies = models.CharField(max_length=25, blank=True)
    drawing_equipment = models.CharField(max_length=25, blank=True)
    tech = models.CharField(max_length=25, blank=True)
    stock_prints_processing = models.CharField(max_length=25, blank=True)
    blueprinting = models.CharField(max_length=25, blank=True)
    other_art = models.CharField(max_length=25, blank=True)
    artSup_total = models.CharField(max_length=25, blank=True)
    dress_rentals = models.CharField(max_length=25, blank=True)
    dress_purchases = models.CharField(max_length=25, blank=True)
    dress_manufacture = models.CharField(max_length=25, blank=True)
    dress_repairs_replacements = models.CharField(max_length=25, blank=True)
    other_dressing = models.CharField(max_length=25, blank=True)
    dressing_total = models.CharField(max_length=25, blank=True)
    props_rentals = models.CharField(max_length=25, blank=True)
    props_purchases = models.CharField(max_length=25, blank=True)
    graphics_signs = models.CharField(max_length=25, blank=True)
    props_repairs_replac = models.CharField(max_length=25, blank=True)
    picture_vehicle_rentals = models.CharField(max_length=25, blank=True)
    picture_vehicle_purchases = models.CharField(max_length=25, blank=True)
    picture_vehicle_mods = models.CharField(max_length=25, blank=True)
    picture_vehicle_ins = models.CharField(max_length=25, blank=True)
    other_props = models.CharField(max_length=25, blank=True)
    props_total = models.CharField(max_length=25, blank=True)
    fx_rentals = models.CharField(max_length=25, blank=True)
    fx_purchases = models.CharField(max_length=25, blank=True)
    stunts_purchases_rentals = models.CharField(max_length=25, blank=True)
    armaments_permits_fees = models.CharField(max_length=25, blank=True)
    other_fx = models.CharField(max_length=25, blank=True)
    fx_total = models.CharField(max_length=25, blank=True)
    animals_rentals = models.CharField(max_length=25, blank=True)
    animals_purchases = models.CharField(max_length=25, blank=True)
    food_stabling = models.CharField(max_length=25, blank=True)
    transport = models.CharField(max_length=25, blank=True)
    vet = models.CharField(max_length=25, blank=True)
    customs_broker = models.CharField(max_length=25, blank=True)
    other_animals = models.CharField(max_length=25, blank=True)
    animals_total = models.CharField(max_length=25, blank=True)
    wardrobe_rentals = models.CharField(max_length=25, blank=True)
    wardrobe_purchases = models.CharField(max_length=25, blank=True)
    ward_manufact = models.CharField(max_length=25, blank=True)
    ward_ship_brok = models.CharField(max_length=25, blank=True)
    ward_repairs_clean = models.CharField(max_length=25, blank=True)
    other_ward = models.CharField(max_length=25, blank=True)
    wardrobe_total = models.CharField(max_length=25, blank=True)
    makeup_rentals = models.CharField(max_length=25, blank=True)
    makeup_purchases = models.CharField(max_length=25, blank=True)
    hair_rentals = models.CharField(max_length=25, blank=True)
    hair_purchases = models.CharField(max_length=25, blank=True)
    wigs = models.CharField(max_length=25, blank=True)
    makeup_fx = models.CharField(max_length=25, blank=True)
    makeup_ship_brok = models.CharField(max_length=25, blank=True)
    other_makeup = models.CharField(max_length=25, blank=True)
    makeup_total = models.CharField(max_length=25, blank=True)
    basic_package_rent_cam = models.CharField(max_length=25, blank=True)
    daily_rentals_cam = models.CharField(max_length=25, blank=True)
    specialty_rent_cam = models.CharField(max_length=25, blank=True)
    camera_purchases = models.CharField(max_length=25, blank=True)
    steadicam = models.CharField(max_length=25, blank=True)
    video_teleprompter = models.CharField(max_length=25, blank=True)
    camera_ship_brok = models.CharField(max_length=25, blank=True)
    loss_damage_cam = models.CharField(max_length=25, blank=True)
    other_camera = models.CharField(max_length=25, blank=True)
    camera_total = models.CharField(max_length=25, blank=True)
    basic_package_rent_elec = models.CharField(max_length=25, blank=True)
    daily_rentals_elec = models.CharField(max_length=25, blank=True)
    specialty_rent_elec = models.CharField(max_length=25, blank=True)
    electric_purchases = models.CharField(max_length=25, blank=True)
    generators = models.CharField(max_length=25, blank=True)
    loss_damage_elec = models.CharField(max_length=25, blank=True)
    other_electric = models.CharField(max_length=25, blank=True)
    electric_total = models.CharField(max_length=25, blank=True)
    basic_package_rent_grip = models.CharField(max_length=25, blank=True)
    daily_rentals_grip = models.CharField(max_length=25, blank=True)
    specialty_rent_grip = models.CharField(max_length=25, blank=True)
    crane_rentals = models.CharField(max_length=25, blank=True)
    scaffolding_grip = models.CharField(max_length=25, blank=True)
    grip_purchases = models.CharField(max_length=25, blank=True)
    loss_damage_grip = models.CharField(max_length=25, blank=True)
    other_grip = models.CharField(max_length=25, blank=True)
    grip_total = models.CharField(max_length=25, blank=True)
    basic_package_rent_sound = models.CharField(max_length=25, blank=True)
    daily_rentals_sound = models.CharField(max_length=25, blank=True)
    wireless_mics = models.CharField(max_length=25, blank=True)
    sound_purchases = models.CharField(max_length=25, blank=True)
    walkie_talkies = models.CharField(max_length=25, blank=True)
    other_sound = models.CharField(max_length=25, blank=True)
    sound_total = models.CharField(max_length=25, blank=True)
    crew_2U = models.CharField(max_length=25, blank=True)
    equipment_2U = models.CharField(max_length=25, blank=True)
    mat_sup_2U = models.CharField(max_length=25, blank=True)
    travliv_2U = models.CharField(max_length=25, blank=True)
    transport_2U = models.CharField(max_length=25, blank=True)
    aerial_unit = models.CharField(max_length=25, blank=True)
    marine_unit = models.CharField(max_length=25, blank=True)
    fringes_taxes_2U = models.CharField(max_length=25, blank=True)
    other_2U = models.CharField(max_length=25, blank=True)
    secondU_total = models.CharField(max_length=25, blank=True)
    film_stock = models.CharField(max_length=25, blank=True)
    video_stock = models.CharField(max_length=25, blank=True)
    digital_stock = models.CharField(max_length=25, blank=True)
    transfer_stock = models.CharField(max_length=25, blank=True)
    hard_drives = models.CharField(max_length=25, blank=True)
    dalies = models.CharField(max_length=25, blank=True)
    telecine = models.CharField(max_length=25, blank=True)
    audio_stock = models.CharField(max_length=25, blank=True)
    magnetic_transfer = models.CharField(max_length=25, blank=True)
    stills = models.CharField(max_length=25, blank=True)
    loss_dam_lab = models.CharField(max_length=25, blank=True)
    other_lab = models.CharField(max_length=25, blank=True)
    stockLab_total = models.CharField(max_length=25, blank=True)
    post_supervisor_qty = models.CharField(max_length=25, blank=True)
    post_supervisor_uno = models.CharField(max_length=25, blank=True)
    post_supervisor_una = models.CharField(max_length=25, blank=True)
    post_supervisor_rt = models.CharField(max_length=25, blank=True)
    post_coordinator_qty = models.CharField(max_length=25, blank=True)
    post_coordinator_uno = models.CharField(max_length=25, blank=True)
    post_coordinator_una = models.CharField(max_length=25, blank=True)
    post_coordinator_rt = models.CharField(max_length=25, blank=True)
    post_assistants_qty = models.CharField(max_length=25, blank=True)
    post_assistants_uno = models.CharField(max_length=25, blank=True)
    post_assistants_una = models.CharField(max_length=25, blank=True)
    post_assistants_rt = models.CharField(max_length=25, blank=True)
    post_accountants_qty = models.CharField(max_length=25, blank=True)
    post_accountants_uno = models.CharField(max_length=25, blank=True)
    post_accountants_una = models.CharField(max_length=25, blank=True)
    post_accountants_rt = models.CharField(max_length=25, blank=True)
    post_accountants_ass_qty = models.CharField(max_length=25, blank=True)
    post_accountants_ass_uno = models.CharField(max_length=25, blank=True)
    post_accountants_ass_una = models.CharField(max_length=25, blank=True)
    post_accountants_ass_rt = models.CharField(max_length=25, blank=True)
    post_consultant = models.CharField(max_length=25, blank=True)
    post_office_rent = models.CharField(max_length=25, blank=True)
    post_office_equ = models.CharField(max_length=25, blank=True)
    post_office_sup = models.CharField(max_length=25, blank=True)
    post_it_network = models.CharField(max_length=25, blank=True)
    post_phone_net = models.CharField(max_length=25, blank=True)
    post_computers_soft = models.CharField(max_length=25, blank=True)
    post_store = models.CharField(max_length=25, blank=True)
    post_ship = models.CharField(max_length=25, blank=True)
    post_craft = models.CharField(max_length=25, blank=True)
    fringes_taxes_post = models.CharField(max_length=25, blank=True)
    post_other = models.CharField(max_length=25, blank=True)
    postSuper_total = models.CharField(max_length=25, blank=True)
    postCoordin_total = models.CharField(max_length=25, blank=True)
    postAssist_total = models.CharField(max_length=25, blank=True)
    postAccount_total = models.CharField(max_length=25, blank=True)
    postAccountAss_total = models.CharField(max_length=25, blank=True)
    postStaffFac_total = models.CharField(max_length=25, blank=True)
    editor_qty = models.CharField(max_length=25, blank=True)
    editor_uno = models.CharField(max_length=25, blank=True)
    editor_una = models.CharField(max_length=25, blank=True)
    editor_rt = models.CharField(max_length=25, blank=True)
    editor_vfx_qty = models.CharField(max_length=25, blank=True)
    editor_vfx_uno = models.CharField(max_length=25, blank=True)
    editor_vfx_una = models.CharField(max_length=25, blank=True)
    editor_vfx_rt = models.CharField(max_length=25, blank=True)
    editor_ass_qty = models.CharField(max_length=25, blank=True)
    editor_ass_uno = models.CharField(max_length=25, blank=True)
    editor_ass_una = models.CharField(max_length=25, blank=True)
    editor_ass_rt = models.CharField(max_length=25, blank=True)
    colorist_grader_qty = models.CharField(max_length=25, blank=True)
    colorist_grader_uno = models.CharField(max_length=25, blank=True)
    colorist_grader_una = models.CharField(max_length=25, blank=True)
    colorist_grader_rt = models.CharField(max_length=25, blank=True)
    graphics_qty = models.CharField(max_length=25, blank=True)
    graphics_uno = models.CharField(max_length=25, blank=True)
    graphics_una = models.CharField(max_length=25, blank=True)
    graphics_rt = models.CharField(max_length=25, blank=True)
    edit_rooms = models.CharField(max_length=25, blank=True)
    edit_equip = models.CharField(max_length=25, blank=True)
    edit_equip_nonlin = models.CharField(max_length=25, blank=True)
    online = models.CharField(max_length=25, blank=True)
    vfx_ed_system = models.CharField(max_length=25, blank=True)
    post_edit_pur = models.CharField(max_length=25, blank=True)
    lossdam_edit = models.CharField(max_length=25, blank=True)
    fringes_taxes_post_edit = models.CharField(max_length=25, blank=True)
    other_post_edit = models.CharField(max_length=25, blank=True)
    editor_total = models.CharField(max_length=25, blank=True)
    editorVfx_total = models.CharField(max_length=25, blank=True)
    editorAss_total = models.CharField(max_length=25, blank=True)
    grader_total = models.CharField(max_length=25, blank=True)
    graphics_total = models.CharField(max_length=25, blank=True)
    editing_total = models.CharField(max_length=25, blank=True)
    sound_designer_qty = models.CharField(max_length=25, blank=True)
    sound_designer_uno = models.CharField(max_length=25, blank=True)
    sound_designer_una = models.CharField(max_length=25, blank=True)
    sound_designer_rt = models.CharField(max_length=25, blank=True)
    editor_sound_qty = models.CharField(max_length=25, blank=True)
    editor_sound_uno = models.CharField(max_length=25, blank=True)
    editor_sound_una = models.CharField(max_length=25, blank=True)
    editor_sound_rt = models.CharField(max_length=25, blank=True)
    editor_music_qty = models.CharField(max_length=25, blank=True)
    editor_music_uno = models.CharField(max_length=25, blank=True)
    editor_music_una = models.CharField(max_length=25, blank=True)
    editor_music_rt = models.CharField(max_length=25, blank=True)
    ed_sound_ass_qty = models.CharField(max_length=25, blank=True)
    ed_sound_ass_uno = models.CharField(max_length=25, blank=True)
    ed_sound_ass_una = models.CharField(max_length=25, blank=True)
    ed_sound_ass_rt = models.CharField(max_length=25, blank=True)
    adr_super_qty = models.CharField(max_length=25, blank=True)
    adr_super_uno = models.CharField(max_length=25, blank=True)
    adr_super_una = models.CharField(max_length=25, blank=True)
    adr_super_rt = models.CharField(max_length=25, blank=True)
    foley_labour_qty = models.CharField(max_length=25, blank=True)
    foley_labour_uno = models.CharField(max_length=25, blank=True)
    foley_labour_una = models.CharField(max_length=25, blank=True)
    foley_labour_rt = models.CharField(max_length=25, blank=True)
    sound_edit_rooms = models.CharField(max_length=25, blank=True)
    sound_edit_equ = models.CharField(max_length=25, blank=True)
    music_edit_equ = models.CharField(max_length=25, blank=True)
    post_sound_edit_pur = models.CharField(max_length=25, blank=True)
    adr = models.CharField(max_length=25, blank=True)
    foley = models.CharField(max_length=25, blank=True)
    pre_mix = models.CharField(max_length=25, blank=True)
    mix = models.CharField(max_length=25, blank=True)
    printmaster = models.CharField(max_length=25, blank=True)
    transfers_deliverables = models.CharField(max_length=25, blank=True)
    lossdam_sound = models.CharField(max_length=25, blank=True)
    fringes_taxes_post_sound = models.CharField(max_length=25, blank=True)
    other_post_sound = models.CharField(max_length=25, blank=True)
    desSound_total = models.CharField(max_length=25, blank=True)
    editorSound_total = models.CharField(max_length=25, blank=True)
    editorMusic_total = models.CharField(max_length=25, blank=True)
    soundEdAss_total = models.CharField(max_length=25, blank=True)
    adrSup_total = models.CharField(max_length=25, blank=True)
    folLab_total = models.CharField(max_length=25, blank=True)
    postSound_total = models.CharField(max_length=25, blank=True)
    vfx_producer = models.CharField(max_length=25, blank=True)
    vfx_supervisor = models.CharField(max_length=25, blank=True)
    vfx_coordinator = models.CharField(max_length=25, blank=True)
    vfx_storyboard = models.CharField(max_length=25, blank=True)
    vfx_pre_vis_team = models.CharField(max_length=25, blank=True)
    vfx_post_vis_team = models.CharField(max_length=25, blank=True)
    vfx_post_other_lab = models.CharField(max_length=25, blank=True)
    miniatures_build = models.CharField(max_length=25, blank=True)
    miniatures_shoot = models.CharField(max_length=25, blank=True)
    motion_capture = models.CharField(max_length=25, blank=True)
    cyberscanning = models.CharField(max_length=25, blank=True)
    vfx_rentals = models.CharField(max_length=25, blank=True)
    vfx_purchases = models.CharField(max_length=25, blank=True)
    vfx_vendor_1 = models.CharField(max_length=25, blank=True)
    vfx_vendor_2 = models.CharField(max_length=25, blank=True)
    vfx_vendor_3 = models.CharField(max_length=25, blank=True)
    vfx_vendor_4 = models.CharField(max_length=25, blank=True)
    vfx_vendor_5 = models.CharField(max_length=25, blank=True)
    vfx_vendor_6 = models.CharField(max_length=25, blank=True)
    vfx_vendor_7 = models.CharField(max_length=25, blank=True)
    vfx_vendor_8 = models.CharField(max_length=25, blank=True)
    vfx_vendor_9 = models.CharField(max_length=25, blank=True)
    vfx_vendor_10 = models.CharField(max_length=25, blank=True)
    vfx_vendors_x = models.CharField(max_length=25, blank=True)
    vfx_expenses = models.CharField(max_length=25, blank=True)
    vfx_traliv = models.CharField(max_length=25, blank=True)
    box_ren_vfx = models.CharField(max_length=25, blank=True)
    lossdam_vfx = models.CharField(max_length=25, blank=True)
    fringes_taxes_vfx = models.CharField(max_length=25, blank=True)
    other_post_vfx = models.CharField(max_length=25, blank=True)
    postVfx_total = models.CharField(max_length=25, blank=True)
    stock = models.CharField(max_length=25, blank=True)
    neg_cutting = models.CharField(max_length=25, blank=True)
    color_cor = models.CharField(max_length=25, blank=True)
    interpos_neg = models.CharField(max_length=25, blank=True)
    prints = models.CharField(max_length=25, blank=True)
    transfers = models.CharField(max_length=25, blank=True)
    other_media_delivery = models.CharField(max_length=25, blank=True)
    distribution_copies = models.CharField(max_length=25, blank=True)
    storage_post = models.CharField(max_length=25, blank=True)
    postLab_total = models.CharField(max_length=25, blank=True)
    titles = models.CharField(max_length=25, blank=True)
    opticals = models.CharField(max_length=25, blank=True)
    stock_footage = models.CharField(max_length=25, blank=True)
    con_script_ccsl = models.CharField(max_length=25, blank=True)
    postTitles_total = models.CharField(max_length=25, blank=True)
    dubs = models.CharField(max_length=25, blank=True)
    subtitles = models.CharField(max_length=25, blank=True)
    closed_caption = models.CharField(max_length=25, blank=True)
    versioning = models.CharField(max_length=25, blank=True)
    trailers = models.CharField(max_length=25, blank=True)
    ads = models.CharField(max_length=25, blank=True)
    transfers_ver = models.CharField(max_length=25, blank=True)
    prints_ver = models.CharField(max_length=25, blank=True)
    dig_copies_ver = models.CharField(max_length=25, blank=True)
    other_copies_ver = models.CharField(max_length=25, blank=True)
    postVersion_total = models.CharField(max_length=25, blank=True)
    tests_theater_ren = models.CharField(max_length=25, blank=True)
    tests_other = models.CharField(max_length=25, blank=True)
    unit_publicist = models.CharField(max_length=25, blank=True)
    pub_press_ex = models.CharField(max_length=25, blank=True)
    photography = models.CharField(max_length=25, blank=True)
    epk = models.CharField(max_length=25, blank=True)
    promotion = models.CharField(max_length=25, blank=True)
    pr = models.CharField(max_length=25, blank=True)
    firnges_pub = models.CharField(max_length=25, blank=True)
    other_pub = models.CharField(max_length=25, blank=True)
    previews = models.CharField(max_length=25, blank=True)
    website = models.CharField(max_length=25, blank=True)
    pub_total = models.CharField(max_length=25, blank=True)
    pro_package = models.CharField(max_length=25, blank=True)
    gen_lia = models.CharField(max_length=25, blank=True)
    eando = models.CharField(max_length=25, blank=True)
    umbrella = models.CharField(max_length=25, blank=True)
    union_insurance = models.CharField(max_length=25, blank=True)
    other_in = models.CharField(max_length=25, blank=True)
    insur_total = models.CharField(max_length=25, blank=True)
    legal = models.CharField(max_length=25, blank=True)
    medical = models.CharField(max_length=25, blank=True)
    licences = models.CharField(max_length=25, blank=True)
    payroll = models.CharField(max_length=25, blank=True)
    bank_charges = models.CharField(max_length=25, blank=True)
    audit = models.CharField(max_length=25, blank=True)
    genEx_total = models.CharField(max_length=25, blank=True)
    corporate_overhead = models.CharField(max_length=25, blank=True)
    fiscal_sponsor_fee = models.CharField(max_length=25, blank=True)
    interim_financing = models.CharField(max_length=25, blank=True)
    indirCo_total = models.CharField(max_length=25, blank=True)
    contingency = models.CharField(max_length=25, blank=True)
    completion_bond = models.CharField(max_length=25, blank=True)
    
    class Meta:
        """ Meta for ordering """
        ordering = ['-created_at']

    def __str__(self):
        return f"{self.title} "
