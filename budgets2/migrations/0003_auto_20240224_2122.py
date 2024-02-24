# Generated by Django 3.2.15 on 2024-02-24 21:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('budgets2', '0002_budget2_budget_number'),
    ]

    operations = [
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_captain_una',
            new_name='dol_grip_rt_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='audio_qty',
            new_name='dol_grip_rt_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='audio_rt',
            new_name='dol_grip_una_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='audio_total',
            new_name='dol_grip_una_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='audio_una',
            new_name='dol_grip_uno_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='audio_uno',
            new_name='dol_grip_uno_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='boardman_qty',
            new_name='dolgripall_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='boardman_rt',
            new_name='dolgripprep_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='boardman_total',
            new_name='dolgripwrap_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='boardman_una',
            new_name='grips_qty_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='boardman_uno',
            new_name='grips_qty_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='drivers_qty',
            new_name='grips_rt_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='drivers_rt',
            new_name='grips_rt_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='drivers_total',
            new_name='grips_una_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='drivers_una',
            new_name='grips_una_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='drivers_uno',
            new_name='grips_uno_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='floor_man_qty',
            new_name='grips_uno_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='floor_man_rt',
            new_name='gripsall_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='floor_man_una',
            new_name='gripsprep_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='floor_man_uno',
            new_name='gripswrap_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='floorman_total',
            new_name='holidays_grip',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='fringes_taxes_transport',
            new_name='holidays_sound',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='fringes_taxes_tv',
            new_name='holidays_unit_grip',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='head_driver_qty',
            new_name='holidays_unit_sound',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='head_driver_rt',
            new_name='k_grip_qty_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='head_driver_una',
            new_name='k_grip_qty_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='head_driver_uno',
            new_name='k_grip_rt_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='headdriver_total',
            new_name='k_grip_rt_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='light_direct_qty',
            new_name='k_grip_una_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='light_direct_rt',
            new_name='k_grip_una_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='light_direct_una',
            new_name='k_grip_uno_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='light_direct_uno',
            new_name='k_grip_uno_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='lightdirect_total',
            new_name='kgripall_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='other_tv_qty',
            new_name='kgripprep_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='other_tv_rt',
            new_name='kgripwrap_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='other_tv_una',
            new_name='ot_sound_qty_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='other_tv_uno',
            new_name='ot_sound_qty_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='othertv_total',
            new_name='ot_sound_rt_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='stagehands_qty',
            new_name='ot_sound_rt_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='stagehands_rt',
            new_name='ot_sound_una_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='stagehands_total',
            new_name='ot_sound_una_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='stagehands_una',
            new_name='ot_sound_uno_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='stagehands_uno',
            new_name='ot_sound_uno_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tech_direct_qty',
            new_name='oth_grip_qty_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tech_direct_rt',
            new_name='oth_grip_qty_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tech_direct_una',
            new_name='oth_grip_rt_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tech_direct_uno',
            new_name='oth_grip_rt_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tech_super_qty',
            new_name='oth_grip_una_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tech_super_rt',
            new_name='oth_grip_una_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tech_super_una',
            new_name='oth_grip_uno_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tech_super_uno',
            new_name='oth_grip_uno_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='techdirect_total',
            new_name='other_solo_grip',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='techsuper_total',
            new_name='other_solo_sound',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_captain_qty',
            new_name='othgripall_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_captain_rt',
            new_name='othgripprep_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_captain_uno',
            new_name='othgripwrap_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_coordinator_qty',
            new_name='otsoundall_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_coordinator_rt',
            new_name='otsoundprep_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_coordinator_una',
            new_name='otsoundwrap_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_coordinator_uno',
            new_name='overtime_grip',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_manager_qty',
            new_name='overtime_sound',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_manager_rt',
            new_name='overtime_unit_grip',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_manager_una',
            new_name='overtime_unit_sound',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tp_manager_uno',
            new_name='so_mix_qty_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tpcaptain_total',
            new_name='so_mix_qty_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tpcoordinator_total',
            new_name='so_mix_rt_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tpmanager_total',
            new_name='so_mix_rt_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='transportlabour_total',
            new_name='so_mix_una_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='tvspecificlabour_total',
            new_name='so_mix_una_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='vtr_operator_qty',
            new_name='so_mix_uno_prep',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='vtr_operator_rt',
            new_name='so_mix_uno_wrap',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='vtr_operator_una',
            new_name='somixall_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='vtr_operator_uno',
            new_name='somixprep_total',
        ),
        migrations.RenameField(
            model_name='budget2',
            old_name='vtroperator_total',
            new_name='somixwrap_total',
        ),
        migrations.AddField(
            model_name='budget2',
            name='bb_grip_qty_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='bb_grip_qty_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='bb_grip_rt_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='bb_grip_rt_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='bb_grip_una_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='bb_grip_una_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='bb_grip_uno_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='bb_grip_uno_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='bbgripall_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='bbgripprep_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='bbgripwrap_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boom_op_qty_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boom_op_qty_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boom_op_rt_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boom_op_rt_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boom_op_una_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boom_op_una_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boom_op_uno_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boom_op_uno_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boomopall_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boomopprep_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='boomopwrap_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='box_rent_grip',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='box_rent_sound',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='box_rent_unit_grip',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='box_rent_unit_sound',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cab_wran_qty_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cab_wran_qty_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cab_wran_rt_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cab_wran_rt_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cab_wran_una_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cab_wran_una_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cab_wran_uno_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cab_wran_uno_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cawranall_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cawranprep_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='cawranwrap_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='days6th7th_grip',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='days6th7th_sound',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='days6th7th_unit_grip',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='days6th7th_unit_sound',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='dol_grip_qty_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='dol_grip_qty_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='sw_grips_qty_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='sw_grips_qty_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='sw_grips_rt_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='sw_grips_rt_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='sw_grips_una_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='sw_grips_una_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='sw_grips_uno_prep',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='sw_grips_uno_wrap',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='swigripsall_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='swigripsprep_total',
            field=models.CharField(blank=True, max_length=25),
        ),
        migrations.AddField(
            model_name='budget2',
            name='swigripswrap_total',
            field=models.CharField(blank=True, max_length=25),
        ),
    ]
