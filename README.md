# HetCoSum
This work proposes HetCoSum to model the syntax structure of code that incorporates the two kinds of features for code summarization. Specifically, we put forward a **Heterogeneous Syntax Graph Neural Network (HSGNN)** to learn the **Heterogeneous Syntax Graph (HSG)** with six types of edges designed on AST. Besides, HetCoSum performs **Transformer** over the **Code with Double-Position (CDP)** to capture the layout features in source code. In addition, by absorbing the learned CDP into the HSG encoder, the overall framework builds the relation between its two encoders for even better code comprehension. In the decoding process, we expand the decoding sub-layer in Transformer decoder and introduce copying mechanism to support high-quality summary generation. Extensive experiments on two real-world datasets in Java and Python demonstrate the superiority of our proposed HetCoSum over the sixteen state-of-the-arts.

# Runtime Environment
- 4 NVIDIA 2080 Ti GPUs 
- Ubuntu 20.04.5
- CUDA 11.3 (with CuDNN of the corresponding version)
- Python 3.9
- PyTorch 1.11
- PyTorch Geometric 2.0.4 
- Specifically, install our package with ```pip install my-lib-0.1.0.tar.gz```. The package can be downloaded from [Google Drive](https://drive.google.com/file/d/1I5Qt1bIeDXBIzmfHwUaxzw4byMRlyNKV/view?usp=sharing)  
# Dataset
The whole datasets of Python and Java can be downloaded from [Google Drive](https://drive.google.com/file/d/1I5Qt1bIeDXBIzmfHwUaxzw4byMRlyNKV/view?usp=sharing).

**Note that:** 
- We provide 100 samples for train/valid/test datasets in the directory `data/python/raw_data/`, `data/java/raw_data/`, and `data/python_GypSum/raw_data/`. 
- *The python_GypSum dataset is originally built by the work [GypSum: Learning Hybrid Representations for Code Summarization](https://arxiv.org/pdf/2204.12916.pdf) for the model evaluation on the cleaned testing set, which is different from the python dataset in `data/python/raw_data/`.*
- To run on the whole datasets,
please download them from [Google Drive](https://drive.google.com/file/d/1I5Qt1bIeDXBIzmfHwUaxzw4byMRlyNKV/view?usp=sharing) for usage.

# Experiment on the Python(Java/Python_GypSum) Dataset
1. Step into the directory `src_code/python(java,python_GypSum)`:
    ```angular2html
    cd src_code/python
    ```
    or
    ```angular2html
    cd src_code/java
    ```
    or
    ```angular2html
    cd src_code/python_GypSum
    ```
2. Proprecess the train/valid/test data:
   ```angular2html
   python s1_preprocessor.py
    ```
    **Note that:**
    It will take hours for pre-processsing the whole dataset.

3. Run the model for training, validation, and testing:
    ```angular2html
   python s2_model.py
   ```
  
After running, the console will display the performances on the whole testing of the python/java datasets and the performance on the cleaned testing set of the python_GypSum dataset. The predicted results of testing data and will be saved in the path `data/python(java,python_GypSum)/result/codescriber_v39b11_6_2_6_512.json`, with ground truth and code involved for comparison.

We have provided the results of the whole testing sets, you can get the evaluation results on the whole python/java testing sets directly by running 
```angular2html
python s3_eval_whole_test_set.py"
```
And you can get the evaluation results on the cleaned java/python_GypSum testing sets by directly run
```angular2html
python s3_eval_cleaned_test_set.py"
```

**Note that:** 
- All the parameters are set in `src_code/python(java,python_GypSum)/config.py`.
- If a model has been trained, you can set the parameter "train_mode" in `config.py` to "False". Then you can predict the testing data directly by using the model that has been saved in `data/python/model/`.
- We have provided in [Google Drive](https://drive.google.com/file/d/1I5Qt1bIeDXBIzmfHwUaxzw4byMRlyNKV/view?usp=sharing) all the files about the trained models as well as the log files of traing processes (in `data/python(java,python_GypSum)/log/`). You can download them for reference and model evaluation without running `s1_preprocessor.py` and model training. Still, don't forget to set the parameter "train_mode" in `config.py` to "False" for direct prediction and evaluation with these files.


# More Implementation Details.

- The main parameter settings for HetCoSum are shown as:

<img src="https://github.com/ANONYMOUSPUB/IMG/blob/main/HETCOSUM/parameter_setting.png" width="50%" height="50%" alt="params">

- The time used per epoch and the memory usage are provided as:

<img src="https://github.com/ANONYMOUSPUB/IMG/blob/main/HETCOSUM/memory_usage.png" width="50%" height="50%" alt="usage">

# Experimental Result:
We provide part of our experiment result as below.
- Comparison with 16 state-of-the-arts, including 12 models without pre-training and 4 pre-training-based models.

<img src="https://github.com/ANONYMOUSPUB/IMG/blob/main/HETCOSUM/comparison_with_baselines.png" width="70%" height="70%" alt="Comparison with the baselines">

- Qualitative examples on the Java and Python datasets.
    
    **Note that:**
    All the words in summary texts were lemmatized in the pre-processing, which is a common operation to reduce the vocabulary size in NLP community. For example, the word "specified" and "segments" became "specify" and "segment" after lemmatization. As a result, some tokens in the processed and generated texts might not fit the context exactly. Practically, such minor grammatical issues does not affect the human understanding of natural language summary texts. To facilitate the observation, we fixed the issues manually in the displayed cases. For example in the fourth Python case, the word "segment" generated by CODESCRIBE was revised as "segments" due to the context "a sequence of". The word "specify" was revised as "specified" in the third Java case. Besides, we removed the space between the words and their following punctuation marks to make the summary texts more natural.
    We make sure that all the minor revisions do not affect the meanings of the generated summaries.

![java_case](https://github.com/ANONYMOUSPUB/IMG/blob/main/HETCOSUM/java_case.png)

![python_case](https://github.com/ANONYMOUSPUB/IMG/blob/main/HETCOSUM/python_case.png)

***This paper is still under review, please do not distribute it.***

    

