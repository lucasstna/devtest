# Dev Test

## Dependencies
Dependencies are listed in the env.yml file. Please notice that the file is ready to be used as a source to creating a new Anaconda env.

To do so, run the following command after installing Anaconda:

```
conda env create -f env.yml
```

With the env ready, generate the **results/elevator_demands.csv** file by running 
```
python elevator/app.py
```
Apart from that, all the endpoints can be tested using the database file (**elevator_registry.db**) by running the FastAPI app:
```
fastapi dev elevator/app.py
```
