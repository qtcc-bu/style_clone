# config for training GPT-2 (124M) down to very nice loss of ~2.85 on 1 node of 8X A100 40GB
# launch as the following (e.g. in a screen session) and wait ~5 days:
# $ torchrun --standalone --nproc_per_node=8 train.py config/train_gpt2.py

out_dir = 'out-baudrillard'

wandb_log = False


dataset = 'baudrillard'
# these make the total batch size be ~0.5M
# 12 batch size * 1024 block size * 5 gradaccum * 8 GPUs = 491,520
batch_size = 12
block_size = 1024

# about 50 epochs or so
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 40*50
log_interval = 100
always_save_checkpoint = True
eval_interval = 40*50
