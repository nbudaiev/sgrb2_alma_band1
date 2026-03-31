import datetime
import os
import sys


def makefits(myimagebase, cleanup=False):
    ###impbcor(imagename=myimagebase+'.image.tt0', pbimage=myimagebase+'.pb.tt0', outfile=myimagebase+'.image.tt0.pbcor', overwrite=True) # perform PBcorr
    ###exportfits(imagename=myimagebase+'.image.tt0.pbcor', fitsimage=myimagebase+'.image.tt0.pbcor.fits', dropdeg=True, overwrite=True) # export the corrected image
   # exportfits(imagename=myimagebase+'.image.tt1', fitsimage=myimagebase+'.image.tt1.fits', dropdeg=True, overwrite=True) # export the corrected image
   # exportfits(imagename=myimagebase+'.pb.tt0', fitsimage=myimagebase+'.pb.tt0.fits', dropdeg=True, overwrite=True) # export the PB image
    ###exportfits(imagename=myimagebase+'.model.tt0', fitsimage=myimagebase+'.model.tt0.fits', dropdeg=True, overwrite=True) # export the PB image
   # exportfits(imagename=myimagebase+'.model.tt1', fitsimage=myimagebase+'.model.tt1.fits', dropdeg=True, overwrite=True) # export the PB image
    ###exportfits(imagename=myimagebase+'.residual.tt0', fitsimage=myimagebase+'.residual.tt0.fits', dropdeg=True, overwrite=True) # export the PB image
   # exportfits(imagename=myimagebase+'.alpha', fitsimage=myimagebase+'.alpha.fits', dropdeg=True, overwrite=True)
   # exportfits(imagename=myimagebase+'.alpha.error', fitsimage=myimagebase+'.alpha.error.fits', dropdeg=True, overwrite=True)

    if cleanup:
        for ttsuffix in ('.tt1', 'tt2'):
            for suffix in ('pb{tt}', 'weight', 'sumwt{tt}', 'psf{tt}',
                           'model{tt}', 'mask', 'image{tt}', 'residual{tt}',
                           'alpha', 'pbcorr{tt}'):
                os.system('rm -rf {0}.{1}'.format(myimagebase, suffix).format(tt=ttsuffix))


threshold = '10mJy'
suffix = 'clean'
cal = 'cal0'



imsize = [4800,4800]
cell = ['0.04arcsec']
niter=100000






ms = '/orange/adamginsburg/sgrb2/2024.1.00993.S/NB/calibrated_final/measurement_sets/uid___A002_X12f38f9_X7dd_targets.ms'

field='Sgr_B2'
spw='17,19,21,23'
robust=0.5

specmode='mfs'
outframe='LSRK'
deconvolver='mtmfs'
nterms=2
gridder='standard'
weighting='briggs'
pbcor=True
pblimit=0.05
savemodel='modelcolumn'
interactive=False


#0.00379Jy = 3mJy was the value in the pipeline delivered threshold

imagename=f'sgr_b2_46ghz_cont_{suffix}_r{robust}_thresh_{threshold}_niter{niter}_{cal}'
if not os.path.exists(imagename+'.image.tt0'):
    tclean(vis=ms,
           imagename=imagename,
            field=field,
            spw=spw,
           imsize=imsize,
           cell=cell,
           robust=robust,
           niter=niter,
           specmode=specmode,
           outframe=outframe,
           deconvolver=deconvolver,
           nterms=nterms,
           gridder=gridder,
           weighting=weighting,
           pbcor=pbcor,
           pblimit=pblimit,
           savemodel=savemodel,
           interactive=interactive)
    makefits(imagename, cleanup=True)