# Invoice angle correction

data is stored in data.zip

## Instalation

```sh
git https://github.com/atgorvi/InvoiceOrientationCorrection.git
cd InvoiceOrientationCorrection

pip install -r requirements.txt
```

## Usage

### Pyhon script
To correct image and save it run:

```sh
python demo.py -i data/images/0.png -s data/images/0_corrected.png
```

### Gradio
To start the gradio demo UI run:

```sh
python gradio_demo.py
```
