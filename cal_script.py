import datetime
import os
import sys


ms_original  = '/orange/adamginsburg/sgrb2/2024.1.00993.S/NB/calibrated_final/measurement_sets/uid___A002_X12f38f9_X7dd_targets.ms'
ms_new = ms_original.replace('.ms', '_selfcal_1.ms')

# #if not os.path.exists(ms_new):
# os.system('rm -rf '+ms_new)
# os.system('cp -r '+ms_original+" "+ms_new) 


#refant='DV09,DV06'
combine='spw'
spwcont='17,19,21,23'

spwmap=[0,0,0,0]
calwt=False
flagbackup=True
solint='int'
minsnr=5
minblperant=4
solnorm=False # set to True when calibrating amplitude 'ap'
calmode='p'
gaintype='T'

cal_tbl = f'cal_table_{calmode}_{minsnr}_int'

#os.system('rm -r '+cal_tbl)

#print("Calibrating folders: " + ms_new)




gaincal(vis=ms_new,
        caltable=cal_tbl,
        gaintype=gaintype,
        calmode=calmode,
        #combine=combine,
        solint=solint,
        minsnr=minsnr,
        minblperant=minblperant,
        solnorm=solnorm,
        field='Sgr_B2',)
        #refant='DV22')
        #normtype=normtype)

calwt = False
spwmap = [17]*72

# applycal(vis=ms_new,
#             spwmap=spwmap,
#             gaintable=cal_tbl,
#             field='Sgr_B2',
#             calwt=calwt,)