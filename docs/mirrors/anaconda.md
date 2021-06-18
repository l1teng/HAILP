## Conda Mirror Help Center

#### Supported Architechtures

- ```linux-64```

- ```win-64```

- ```osx-64```

#### Configuration

```bash
channels:
  - defaults
show_channel_urls: true
default_channels:
  - http://172.18.220.5/anaconda/pkgs/main
  - http://172.18.220.5/anaconda/pkgs/free
```

#### Contribute

If more syncing repos are needed, please pull request to [**sync_conda.py**](https://github.com/litun5315/hfutail-mirrorsync/blob/master/mirrors_sync/sync_conda.py) in our github syncing scripts repository.
