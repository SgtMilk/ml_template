# ml_template
This is a template for a ML pytorch project.

I was tired of always re-coding all the tools I needed for my ML projects, so I made a template.

## Here are the main places you should edit the code:
- Training:
    - `/src/data/clean.py` for how to generally format the data you need.
    - `/src/data/dataloader.py` for how format the data to fit x/y data (or any other format you need).
    - `src/model/XXXXXX_model.py` to create your model, replacing `src/model/linear_model.py`.
    - `src/model/net.py` to modify your training loop, evaluating, and the way the optimizer and model are initialized.
    - `src/params/hyperparameters` to modify the training hyperparameters.
- Testing:
    - The whole `/test` folder.
