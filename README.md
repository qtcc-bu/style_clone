# style_clone
Final project for CS505: intro to NLP at BU. 

Paper explaining the project, method, data collection, and results is included. 

99.99% of this is aped from andrei kaparthey's nanogpt repo. that's here: https://github.com/karpathy/nanoGPT. It is great!

To reproduce the results, run these four commands to train the models:
>python train.py config/finetune_baudrillard.py --compile=False
>python train.py config/train_gpt2_baudrillard.py --compile=False
>python train.py config/finetune_borges.py --compile=False
>python train.py config/train_gpt2_borges.py --compile=False

and then run these scripts to sample the models:

>python sample.py --out_dir=out-baudrillard --start="It ended as it always began," --num_samples=3 --max_new_tokens=100 
>python sample.py --out_dir=out-ft-baudrillard --start="It ended as it always began," --num_samples=3 --max_new_tokens=100 
>python sample.py --out_dir=out-borges --start="It ended as it always began," --num_samples=3 --max_new_tokens=100 
>python sample.py --out_dir=out-ft-borges --start="It ended as it always began," --num_samples=3 --max_new_tokens=100