# Veri Seti (Drive)
Github'a her ne kadar yüklemeye uğraşsam da (LFS dahil denendi, veri setini küçültüp denedim bu sefer de aylık kota gibi şeylere takıldım.) başarılı olamadım, o yüzden Drive'a yükledim.

Drive Linki: https://drive.google.com/drive/folders/1KlUOu0GsrpCs5HxJHMLBmifcQCE-6LlV?usp=sharing

Model eğitimi `mel_spectrograms_train.npy` ve `labels_train.npy` dosyaları ile yapılmaktadır. Bu dosyaları repository'yi klonladıktan sonra repo'yu klonladığımız klasörün içine attığımızda `models` klasörü altından `train.ipynb` dosyalarını kullanarak her bir modeli eğitebiliyoruz.

Ayrıca Drive üzerinde `test_dataset` klasörü altında `mel_spectrograms_test.npy` ve `labels_test.npy` dosyalarının üretilmesinde kullanılan test ses dosyaları bulunmaktadır.

Model testi `mel_spectrograms_test.npy` ve `labels_test.npy` dosyalari ile yapılmaktadır. Bu dosyaları repository'yi klonladıktan sonra repo'yu klonladığımız klasörün içine attığımızda `models` klasörü altından `test.ipynb` dosyalarını kullanarak her bir modeli test edebiliyoruz. Bu dosyalar Drive üzerinde verilen `test_dataset.zip` dosyasının içerisindeki ses kayıtlarının `produce_fake_audio/mel_spectrogram_extraction.ipynb` dosyası kullanılarak mel-spectrogram'larına ayrılmasıyla elde edilmiştir. İstenirse bu tekrarlanabilir. Bunu yapmak için `test_dataset.zip` dosyası `produce_fake_audio` klasörü içerisine çıkartıldıktan sonra `mel_spectrogram_extraction.ipynb` kodu çalıştırılabilir. Ardından oluşan .npy uzantılı test dosyaları `models` klasörü altındaki `test.ipynb` dosyalarına load edilerek kullanılabilir.

# Kurulum (Paket Kurulumları) (Başka şekillerde de paketler kurulabilir. Requirements.txt dosyasını verdim.)

## models Klasörü İçin
cd models <br>
python3 -m venv venv <br>
pip install -r requirements.txt

## producing_fake_audio Klasörü İçin
cd produce_fake_audio <br>
python3 -m venv venv <br>
pip install -r requirements.txt

Not1: İki klasörün requirements.txt dosyaları farklıdır. Çünkü birincisi model eğitimi ve testinde kullanılırken, ikincisi feature_extraction ve dataset'e veri üretimi için kullanılmıştır.

Not2: Paket versiyonlarının çakışmaması için ayrı ayrı environment'lara kurulmasını tavsiye ederim.
# Projenin Genel Dosya Yapısı

## `models` Klasörü

Bu klasörün içerisinde modelin değişik versiyonlarının bulunduğu klasördür. Her bir model için klasör içerisinde `train.ipynb` ve `test.ipynb` dosyaları bulunmaktadır. Bu dosyalar ile model eğitilmiş ve test edilmiştir. Ayrıca çıktılar da bu dosyalara kaydedilmiştir.

## `produce_fake_audio` Klasörü

### `mel_spectrogram_extraction.ipynb` Dosyası

Bu dosya ses dosyalarından mel-spectrogram feature'larının çıkarılmasında kullanılmıştır. Dosya içerisinde `dataset_dir` değişkenine dataset directory verilerek içerisindeki tüm ses dosyalarından recursive olarak (subfolder içindekiler dahil) mel-spectrogram çıkarmaktadır.

### `produce_coqui.py` Dosyası

Bu dosya `coqui-ai/tts` modelini kullanarak sahte ses kayıtlarının üretilmesinde kullanılmıştır. Modelin kendi bünyesinde bulunan sesler kullanılmıştır.

### `produce_coqui_custom.py` Dosyası

Bu dosya `coqui-ai/tts` modelini kullanarak gerçek ses kayıtlarına ait seslerin kullanılmasıyla sahte seslerin üretiminde kullanılmıştır. (Voice cloning)

### `produce_elevenlabs.py` Dosyası

Bu dosya ElevenLabs TTS modellerini kullanarak sahte ses kaydı üretiminde kullanılmıştır.

# Jupyter Dosyalarının Açıklanması

`models` klasörü altında her bir modelin klasörü altında bulunan Jupyter dosyalarından `train.ipynb` modelin eğitiminin yapılmasını sağlayan dosyadır. Bu dosyada modele ait hyperparameter'ler bulunmaktadır ve model eğitimin ardından kaydedilmektedir.

`test.ipynb` ise ilgili modelin test edilmesini sağlamaktadır. Bu dosya daha önceden preprocess edilen test veri setindeki ses dosyalarına ait mel-spectrogram'ları yükleyerek bulunduğu klasördeki modeli test etmektedir.

`mel_spectrogram_extraction.ipynb` dosyası ses dosyalarından mel-spectrogram feature'larının çıkarılmasında kullanılmıştır. Dosya içerisinde `dataset_dir` değişkenine dataset directory verilerek içerisindeki tüm ses dosyalarından recursive olarak (subfolder içindekiler dahil) mel-spectrogram çıkarmaktadır.

