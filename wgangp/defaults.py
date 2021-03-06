CHECKPOINTS_DIR = '../checkpoints'
FINALS_DIR = '../final_models'

def get_defaults():
  DEFAULTS = {
    # Dataset Classes
    'classes': [5554],  # Petronas Towers by default, cuz it's my fave

    # Resume
    'resume': None,

    # Model parameters
    'noise_dim': 96,
    'image_dim': 64,
    'image_channels': 3,
    'disc_channels': 64,
    'gen_channels': 64,

    # Train-time dynamics
    'batch_size': 32,
    'num_epochs': 10,
    'init_method': 'gaussian',
    'disc_iterations': 5,
    'disc_warmup_length': 0,
    'disc_warmup_iterations': 30,
    'disc_rapid_train_interval': 500,
    'lambda_val': 10,

    # Optimizer hyperparameters
    'optim': 'Adam',
    'learning_rate': 1e-3,
    'beta1': 0.5,
    'beta2': 0.9,
    'weight_decay': 1e-4,

    # Reporter and checkpoint configuration
    'images_every': 100,
    'losses_every': 10,
    'checkpoint_every': 300,
    'sample_size': 36,
    'tag': '',

    # Cuda
    'use_cuda': False,
  }
  return DEFAULTS
