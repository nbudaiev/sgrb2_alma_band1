import datetime
import os
import sys


ms_original  = '/orange/adamginsburg/sgrb2/2024.1.00993.S/NB/calibrated_final/measurement_sets/uid___A002_X12f38f9_X7dd_targets.ms'
ms_new = ms_original.replace('.ms', '_selfcal_1.ms')
os.system('cp -r '+ms_original+" "+ms_new) 


gaintype='T'
#refant='DV09,DV06'
combine='spw'
spwcont='17,19,21,23'

spwmap=[0,0,0,0]
calwt=False
flagbackup=True
applymode='calonly'
solint='inf'
minsnr=5.0
minblperant=4
solnorm=False # set to True when calibrating amplitude 'ap'
calmode='p'
gaintype='G'

cal_tbl = f'cal_table_{calmode}_{minsnr}'

#tbl1='pcal'+str(step)+'_1_selfcal_test'
#tbl2='pcal'+fld+conf+str(step)+'_2_selfcal_test'

os.system('rm -r '+cal_tbl)

print("Calibrating folders: " + ms_new)




gaincal(vis=ms_new,
        caltable=cal_tbl,
        gaintype=gaintype,
        refant=refant,
        calmode=calmode,
        combine=combine,
        solint=solint,
        minsnr=minsnr,
        minblperant=minblperant,
        solnorm=solnorm,)
        #normtype=normtype)