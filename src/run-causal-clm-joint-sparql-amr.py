#!/usr/bin/env python
# coding=utf-8
# Copyright 2020 The HuggingFace Inc. team. All rights reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
Fine-tuning the library models for causal language modeling (GPT, GPT-2, CTRL, ...) on a text file or a dataset.
Here is the full list of checkpoints on the hub that can be fine-tuned by this script:
https://huggingface.co/models?filter=causal-lm



start conda environment, install pytorch


pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118

conda install absl-py pandas transformers

conda install -c anaconda nltk networkx

conda install -c conda-forge dataclasses 

pip install rouge-score pyarrow datasets evaluate scikit-learn




CUDA_VISIBLE_DEVICES=0,1,2 python src/run-causal-clm-joint-sparql-amr.py \
--model_name_or_path ~/tmp/tmphgf56dee39441-flan-t5-large-2023-10-02-joint-sparql-amr-wikidata-2eps \
--tokenizer_name google/flan-t5-large \
--train_file data/qald-joint-train-flan-2023-10-02.csv \
--validation_file data/qald-joint-valid-flan-2023-10-02.csv \
--validation_file_gen data/qald-massive-joint-valid-flan-2023-10-02_five_cols.csv \
--per_device_train_batch_size 2 \
--per_device_eval_batch_size 1 \
--do_eval \
--task fine-tune-flan-t5-large-joint-sparql-amr-wikidata-2eps \
--save_strategy no \
--search_type beam \
--num_beams 5 \
--max_gen_length 256 \
--p_sampling 0.90 \
--temperature 0.90 \
--num_train_epochs 2 \
--output_dir ~/tmp/tmphgf56dee39441-flan-t5-large-2023-10-02-joint-sparql-amr-wikidata-2eps \
--overwrite_output_dir \
--overwrite_cache True \
--optim adamw_torch \
--lr_scheduler_type cosine \
--block_size 400 \
--gradient_accumulation_steps 1 \
--learning_rate 1e-4 \
--results_dir ~/reports/



CUDA_VISIBLE_DEVICES=0,1,2 python src/run-causal-clm-joint-sparql-amr.py \
--model_name_or_path ~/tmp/tmphgf56dee39442-distill-2023-10-02-joint-amr-sparql-massive-16eps \
--tokenizer_name ~/models/downloaded/comet-distill-tokenizer \
--train_file data/qald-joint-train-flan-2023-10-02.csv \
--validation_file data/qald-joint-valid-flan-2023-10-02.csv \
--validation_file_gen data/qald-massive-joint-valid-flan-2023-10-02_five_cols.csv \
--per_device_train_batch_size 2 \
--per_device_eval_batch_size 1 \
--do_eval \
--task inference-distill-joint-sparql-amr-massive-16eps \
--do_metrics False \
--save_strategy no \
--search_type beam \
--num_beams 5 \
--temperature 0.95 \
--num_train_epochs 16 \
--output_dir ~/tmp/tmphgf56dee39442-distill-2023-10-02-joint-amr-sparql-massive-16eps \
--overwrite_output_dir \
--overwrite_cache False \
--optim adamw_torch \
--lr_scheduler_type cosine \
--block_size 512 \
--gradient_accumulation_steps 1 \
--learning_rate 5e-5 \
--results_dir ~/reports/


CUDA_VISIBLE_DEVICES=0 python src/run-causal-clm-joint-sparql-amr.py \
--model_name_or_path microsoft/phi-1_5 \
--tokenizer_name microsoft/phi-1_5 \
--train_file data/qald-joint-train-gpt2-2023-09-21.csv \
--validation_file data/qald-joint-valid-gpt2-2023-09-21.csv \
--validation_file_gen data/qald-joint-valid-gpt2-2023-09-21_five_cols.csv \
--per_device_train_batch_size 2 \
--per_device_eval_batch_size 1 \
--do_train \
--task phi-1_5-joint-sparql-amr-wikidata-16eps \
--do_metrics False \
--save_strategy no \
--search_type beam \
--num_beams 5 \
--temperature 0.95 \
--num_train_epochs 8 \
--output_dir ~/tmp/tmphgf56dee39442-phi-1_5-2023-09-21-joint-amr-sparql-wikidata-8eps \
--overwrite_output_dir \
--overwrite_cache False \
--optim adamw_torch \
--lr_scheduler_type cosine \
--block_size 512 \
--gradient_accumulation_steps 1 \
--learning_rate 5e-5 \
--results_dir ~/reports/


CUDA_VISIBLE_DEVICES=0 python src/run-causal-clm-joint-sparql-amr.py \
--model_name_or_path ~/tmp/tmphgf56dee39442-phi-1_5-2023-09-21-joint-amr-sparql-wikidata-8eps \
--tokenizer_name microsoft/phi-1_5 \
--train_file data/qald-joint-train-gpt2-2023-09-21.csv \
--validation_file data/qald-joint-valid-gpt2-2023-09-21.csv \
--validation_file_gen data/qald-joint-valid-gpt2-2023-09-21_five_cols.csv \
--per_device_train_batch_size 2 \
--per_device_eval_batch_size 1 \
--do_eval \
--task phi-1_5-joint-sparql-amr-wikidata-8eps \
--do_metrics False \
--save_strategy no \
--search_type p \
--num_beams 5 \
--temperature 0.95 \
--num_train_epochs 8 \
--output_dir ~/tmp/tmphgf56dee39442-phi-1_5-2023-09-21-joint-amr-sparql-wikidata-8eps \
--overwrite_output_dir \
--overwrite_cache False \
--optim adamw_torch \
--lr_scheduler_type cosine \
--block_size 512 \
--gradient_accumulation_steps 1 \
--learning_rate 5e-5 \
--results_dir ~/reports/


CUDA_VISIBLE_DEVICES=0 python src/run-causal-clm-joint-sparql-amr.py \
--model_name_or_path ~/tmp/tmphgf56dee39441-flan-t5-large-2023-09-25-joint-sparql-amr-wikidata-8eps \
--tokenizer_name google/flan-t5-large \
--train_file data/qald-joint-train-flan-2023-09-25.csv \
--validation_file data/qald-joint-valid-flan-2023-09-25.csv \
--validation_file_gen data/qald-massive-joint-valid-flan-2023-09-25_five_cols.csv \
--per_device_train_batch_size 2 \
--per_device_eval_batch_size 1 \
--do_eval \
--task inference-flan-large-8eps-joint-sparql-amr \
--do_metrics False \
--save_strategy no \
--search_type beam \
--num_beams 5 \
--max_gen_length 128 \
--temperature 0.95 \
--num_train_epochs 8 \
--output_dir ~/tmp/tmphgf56dee39441-flan-t5-large-2023-09-25-joint-sparql-amr-wikidata-8eps \
--overwrite_output_dir \
--overwrite_cache False \
--optim adamw_torch \
--lr_scheduler_type cosine \
--block_size 512 \
--gradient_accumulation_steps 1 \
--learning_rate 1e-4 \
--results_dir ~/reports/








"""
# You can also adapt this script on your own causal language modeling task. Pointers for this are left as comments.

import datetime
import json
import logging
import math
import networkx as nx
import numpy as np
import pandas as pd
import os
import re
import sys
import torch
from tqdm import tqdm

from dataclasses import dataclass, field
from typing import Optional

import datasets
from datasets import load_dataset, load_metric, disable_caching

import evaluate
import transformers
from transformers import (
    CONFIG_MAPPING,
    MODEL_FOR_CAUSAL_LM_MAPPING,
    AutoConfig,
    AutoModelForCausalLM,
    AutoTokenizer,
    HfArgumentParser,
    Trainer,
    TrainingArguments,
    default_data_collator,
    is_torch_tpu_available,
    set_seed,
)
from transformers.testing_utils import CaptureLogger
from transformers.trainer_utils import get_last_checkpoint
from transformers.utils import check_min_version
from transformers.utils.versions import require_version

from transformers import GPT2Tokenizer, GPT2LMHeadModel, AutoModelForSeq2SeqLM

#from transformers import BartForConditionalGeneration, BartTokenizer

import nltk
from nltk.translate.bleu_score import SmoothingFunction

from evaluate import load
#bertscore = load("bertscore")


# Will error if the minimal version of Transformers is not installed. Remove at your own risks.
check_min_version("4.9.0.dev0")

require_version("datasets>=1.8.0", "To fix: pip install -r examples/pytorch/language-modeling/requirements.txt")

logger = logging.getLogger(__name__)


MODEL_CONFIG_CLASSES = list(MODEL_FOR_CAUSAL_LM_MAPPING.keys())
MODEL_TYPES = tuple(conf.model_type for conf in MODEL_CONFIG_CLASSES)


@dataclass
class ModelArguments:
    """
    Arguments pertaining to which model/config/tokenizer we are going to fine-tune, or train from scratch.
    """

    model_name_or_path: Optional[str] = field(
        default=None,
        metadata={
            "help": "The model checkpoint for weights initialization."
            "Don't set if you want to train a model from scratch."
        },
    )
    model_type: Optional[str] = field(
        default=None,
        metadata={"help": "If training from scratch, pass a model type from the list: " + ", ".join(MODEL_TYPES)},
    )
    config_overrides: Optional[str] = field(
        default=None,
        metadata={
            "help": "Override some existing default config settings when a model is trained from scratch. Example: "
            "n_embd=10,resid_pdrop=0.2,scale_attn_weights=false,summary_type=cls_index"
        },
    )
    config_name: Optional[str] = field(
        default=None, metadata={"help": "Pretrained config name or path if not the same as model_name"}
    )
    tokenizer_name: Optional[str] = field(
        default=None, metadata={"help": "Pretrained tokenizer name or path if not the same as model_name"}
    )
    cache_dir: Optional[str] = field(
        default=None,
        metadata={"help": "Where do you want to store the pretrained models downloaded from huggingface.co"},
    )
    use_fast_tokenizer: bool = field(
        default=True,
        metadata={"help": "Whether to use one of the fast tokenizer (backed by the tokenizers library) or not."},
    )
    model_revision: str = field(
        default="main",
        metadata={"help": "The specific model version to use (can be a branch name, tag name or commit id)."},
    )
    use_auth_token: bool = field(
        default=False,
        metadata={
            "help": "Will use the token generated when running `transformers-cli login` (necessary to use this script "
            "with private models)."
        },
    )

    def __post_init__(self):
        if self.config_overrides is not None and (self.config_name is not None or self.model_name_or_path is not None):
            raise ValueError(
                "--config_overrides can't be used in combination with --config_name or --model_name_or_path"
            )


@dataclass
class DataTrainingArguments:
    """
    Arguments pertaining to what data we are going to input our model for training and eval.
    """

    dataset_name: Optional[str] = field(
        default=None, metadata={"help": "The name of the dataset to use (via the datasets library)."}
    )
    dataset_config_name: Optional[str] = field(
        default=None, metadata={"help": "The configuration name of the dataset to use (via the datasets library)."}
    )
    train_file: Optional[str] = field(default=None, metadata={"help": "The input training data file (a text file)."})
    validation_file: Optional[str] = field(
        default=None,
        metadata={"help": "An optional input evaluation data file to evaluate the perplexity on (a text file)."},
    )
    test_file: Optional[str] = field(
        default=None,
        metadata={"help": "An optional input evaluation with one column."},
    )
    validation_file_gen: Optional[str] = field(
        default=None,
        metadata={"help": "An optional input evaluation for generation with two columns."},
    )
    test_file_gen: Optional[str] = field(
        default=None,
        metadata={"help": "An optional input evaluation with two columns to generate with labels."},
    )
    max_train_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of training examples to this "
            "value if set."
        },
    )
    max_eval_samples: Optional[int] = field(
        default=None,
        metadata={
            "help": "For debugging purposes or quicker training, truncate the number of evaluation examples to this "
            "value if set."
        },
    )

    block_size: Optional[int] = field(
        default=None,
        metadata={
            "help": "Optional input sequence length after tokenization. "
            "The training dataset will be truncated in block of this size for training. "
            "Default to the model max input length for single sentence inputs (take into account special tokens)."
        },
    )
    batch_size: Optional[int] = field(
        default=None,
        metadata={
            "help": "Optional batch_size"
        },
    )
    overwrite_cache: bool = field(
        default=False, metadata={"help": "Overwrite the cached training and evaluation sets"}
    )
    validation_split_percentage: Optional[int] = field(
        default=5,
        metadata={
            "help": "The percentage of the train set used as validation set in case there's no validation split"
        },
    )
    max_gen_length: Optional[int] = field(
        default=512,
        metadata={
            "help": "Maximum number of generated tokens"
        },
    )
    preprocessing_num_workers: Optional[int] = field(
        default=None,
        metadata={"help": "The number of processes to use for the preprocessing."},
    )
    search_type: Optional[str] = field(
        default="beam",
        metadata={"help": "greedy, beam or p"},
    )
    temperature: Optional[float] = field(
        default=0.7,
        metadata={"help": "temperature"},
    )
    num_beams: Optional[int] = field(
        default=1,
        metadata={"help": "number of beams"},
    )
    p_sampling: Optional[float] = field(
        default=0.9,
        metadata={"help": "sampling value"},
    )
    results_dir: Optional[str] = field(
        default=None,
        metadata={"help": "directory to write csv results from validation file"},
    )
    do_metrics: Optional[bool] = field(
        default=False,
        metadata={"help": "do metrics when you have gold reference to compare to"},
    )
    task: Optional[str] = field(
        default='generation',
        metadata={"help": "tasks: nodePrediction, generation"},
    )

    def __post_init__(self):
        if self.dataset_name is None and self.train_file is None and self.validation_file is None:
            raise ValueError("Need either a dataset name or a training/validation file.")
        else:
            if self.train_file is not None:
                extension = self.train_file.split(".")[-1]
                assert extension in ["csv", "json", "txt"], "`train_file` should be a csv, a json or a txt file."
            if self.validation_file is not None:
                extension = self.validation_file.split(".")[-1]
                assert extension in ["csv", "json", "txt"], "`validation_file` should be a csv, a json or a txt file."
            if self.test_file is not None:
                extension = self.test_file.split(".")[-1]
                assert extension in ["csv", "json", "txt"], "`test_file` should be a csv, a json or a txt file."



def similarity(s1, s2):
    # actually let's try comparing two dictionaries
    return s1==s2


def bleu_similarity(reference, candidate):

    #metric = load_metric("bleu")

    chencherry = SmoothingFunction()

    reference, candidate = reference.split(), candidate.split()

    bleu = nltk.translate.bleu_score.sentence_bleu([reference], 
                                                    candidate, 
                                                    weights = (0.5, 0.5),  
                                                    smoothing_function=chencherry.method1)
    return bleu



def compute_transition_scores_func(generated_tokens, generated_tokens_scores, model, gen_outputs, tokenizer):
    
    cnt = 0
    transition_scores_to_save = []

    these_transition_scores = model.compute_transition_scores(
        gen_outputs.sequences, gen_outputs.scores, normalize_logits=True
    )

    print(f"len gen_outputs.scores: {len(gen_outputs.scores)}")
    print(f"len gen_outputs.scores indx 0: {len(gen_outputs.scores[0][0])}")
    # print(f"AMR score: {generated_tokens_scores[0][0][tokenizer.encode('AMR')]}")
    # print(f"SPARQL score: {generated_tokens_scores[0][0][tokenizer.encode('SPARQL')]}")
    for tok, score in zip(generated_tokens[0], these_transition_scores[0]):
        score = score.cpu()
        if cnt < 10:
            cnt+=1
            transition_str = f"| {tok:5d} | {tokenizer.decode(tok):8s} | {score.numpy():.3f} | {np.exp(score.numpy()):.2%}"
            transition_scores_to_save.append(transition_str)
            print(transition_str)
    print()

    return transition_scores_to_save



def compute_beam_transition_scores_func(beam_outputs, tokenizer):

    cnt = 0
    transition_scores_to_save = []
    for sequence, this_score in zip(beam_outputs.sequences, beam_outputs.scores):
        beam_transition_scores = []
        for tok, score in zip(sequence, this_score):
            if cnt<10:
                cnt+=1
                score = score.cpu()
                transition_str = f"| {tok:5d} | {tokenizer.decode(tok):8s} | {score.numpy():.3f} | {np.exp(score.numpy()):.2%}"
                beam_transition_scores.append(transition_str)
                print(transition_str)
        transition_scores_to_save.append(beam_transition_scores)
        print()

    return transition_scores_to_save


def compute_beam_transition_scores_func_v2(inputs, outputs, model, tokenizer):
    cnt = 0
    transition_scores_to_save = []

    transition_scores = model.compute_transition_scores(
        outputs.sequences, outputs.scores, outputs.beam_indices, normalize_logits=False
    )
    
    for g_output, t_score in zip(outputs.sequences, transition_scores):
        input_length = 1 if model.config.is_encoder_decoder else inputs.input_ids.shape[1]
        generated_tokens = g_output[input_length:]

        for tok, score in zip(generated_tokens, t_score):
            score = score.cpu()
            if cnt < 1:
                cnt+=1
                transition_str = f"| {tok:5d} | {tokenizer.decode(tok):8s} | {score.numpy():.3f} | {np.exp(score.numpy()):.2%}"
                transition_scores_to_save.append(transition_str)
                print(transition_str)
        print()
        cnt = 0
    return transition_scores_to_save




def main():
    # See all possible arguments in src/transformers/training_args.py
    # or by passing the --help flag to this script.
    # We now keep distinct sets of args, for a cleaner separation of concerns.

    # disable_caching()

    parser = HfArgumentParser((ModelArguments, DataTrainingArguments, TrainingArguments))
    if len(sys.argv) == 2 and sys.argv[1].endswith(".json"):
        # If we pass only one argument to the script and it's the path to a json file,
        # let's parse it to get our arguments.
        model_args, data_args, training_args = parser.parse_json_file(json_file=os.path.abspath(sys.argv[1]))
    else:
        model_args, data_args, training_args = parser.parse_args_into_dataclasses()

    # Setup logging
    logging.basicConfig(
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
        datefmt="%m/%d/%Y %H:%M:%S",
        handlers=[logging.StreamHandler(sys.stdout)],
    )

    log_level = training_args.get_process_log_level()
    logger.setLevel(log_level)
    datasets.utils.logging.set_verbosity(log_level)
    transformers.utils.logging.set_verbosity(log_level)
    transformers.utils.logging.enable_default_handler()
    transformers.utils.logging.enable_explicit_format()

    # Log on each process the small summary:
    logger.warning(
        f"Process rank: {training_args.local_rank}, device: {training_args.device}, n_gpu: {training_args.n_gpu}"
        + f"distributed training: {bool(training_args.local_rank != -1)}, 16-bits training: {training_args.fp16}"
    )
    logger.info(f"Training/evaluation parameters {training_args}")

    # Detecting last checkpoint.
    last_checkpoint = None
    if os.path.isdir(training_args.output_dir) and training_args.do_train and not training_args.overwrite_output_dir:
        last_checkpoint = get_last_checkpoint(training_args.output_dir)
        if last_checkpoint is None and len(os.listdir(training_args.output_dir)) > 0:
            raise ValueError(
                f"Output directory ({training_args.output_dir}) already exists and is not empty. "
                "Use --overwrite_output_dir to overcome."
            )
        elif last_checkpoint is not None and training_args.resume_from_checkpoint is None:
            logger.info(
                f"Checkpoint detected, resuming training at {last_checkpoint}. To avoid this behavior, change "
                "the `--output_dir` or add `--overwrite_output_dir` to train from scratch."
            )

    # Set seed before initializing model.
    set_seed(training_args.seed)

    # Get the datasets: you can either provide your own CSV/JSON/TXT training and evaluation files (see below)
    # or just provide the name of one of the public datasets available on the hub at https://huggingface.co/datasets/
    # (the dataset will be downloaded automatically from the datasets Hub).
    #
    # For CSV/JSON files, this script will use the column called 'text' or the first column if no column called
    # 'text' is found. You can easily tweak this behavior (see below).
    #
    # In distributed training, the load_dataset function guarantee that only one local process can concurrently
    # download the dataset.
    if data_args.dataset_name is not None:
        # Downloading and loading a dataset from the hub.
        raw_datasets = load_dataset(
            data_args.dataset_name, data_args.dataset_config_name, cache_dir=model_args.cache_dir
        )

        if "validation" not in raw_datasets.keys():
            raw_datasets["validation"] = load_dataset(
                data_args.dataset_name,
                data_args.dataset_config_name,
                split=f"train[:{data_args.validation_split_percentage}%]",
                cache_dir=model_args.cache_dir,
            )
            raw_datasets["train"] = load_dataset(
                data_args.dataset_name,
                data_args.dataset_config_name,
                split=f"train[{data_args.validation_split_percentage}%:]",
                cache_dir=model_args.cache_dir,
            )
    else:
        data_files = {}
        data_files_two_cols = {}
        if data_args.train_file is not None:
            data_files["train"] = data_args.train_file
        if data_args.validation_file is not None:
            #data_files["validation_gen"] = data_args.validation_file
            data_files["validation"] = data_args.validation_file
        if data_args.test_file is not None:
            #data_files["test_gen"] = data_args.test_file
            data_files["test"] = data_args.test_file

        if data_args.validation_file_gen is not None:
            #data_files_two_cols["test_gen"] = data_args.test_file_gen
            data_files_two_cols["validation_gen"] = data_args.validation_file_gen

        extension = (
            data_args.train_file.split(".")[-1]
            if data_args.train_file is not None
            else data_args.validation_file.split(".")[-1]
        )
        print("Data files")
        print(data_files)   
        print()
        print(data_files_two_cols) 
        print()    

        if extension == "txt":
            extension = "text"
        raw_datasets = load_dataset(extension, 
                                    data_files=data_files, 
                                    cache_dir=model_args.cache_dir)

        raw_datasets_gen = load_dataset(extension, 
                                    data_files=data_files_two_cols, 
                                    cache_dir=model_args.cache_dir,
                                    column_names=["text", "y_sparql", "y_amr", "language", "corpus"],
                                    skiprows=1)

        #raw_datasets["test"] = raw_datasets["validation"]

        print(raw_datasets)
        print()
        print(raw_datasets_gen)

    # See more about loading any type of standard or custom dataset (from files, python dict, pandas DataFrame, etc) at
    # https://huggingface.co/docs/datasets/loading_datasets.html.

    # Load pretrained model and tokenizer
    #
    # Distributed training:
    # The .from_pretrained methods guarantee that only one local process can concurrently
    # download model & vocab.

    config_kwargs = {
        "cache_dir": model_args.cache_dir,
        "revision": model_args.model_revision,
        "use_auth_token": True if model_args.use_auth_token else None,
        "trust_remote_code": True if 'phi' in model_args.model_name_or_path else False
    }
    if model_args.config_name:
        config = AutoConfig.from_pretrained(model_args.config_name, **config_kwargs)
    elif model_args.model_name_or_path:
        config = AutoConfig.from_pretrained(model_args.model_name_or_path, **config_kwargs)
    else:
        config = CONFIG_MAPPING[model_args.model_type]()
        logger.warning("You are instantiating a new config instance from scratch.")
        if model_args.config_overrides is not None:
            logger.info(f"Overriding config: {model_args.config_overrides}")
            config.update_from_string(model_args.config_overrides)

    tokenizer_kwargs = {
        "cache_dir": model_args.cache_dir,
        "use_fast": model_args.use_fast_tokenizer,
        "revision": model_args.model_revision,
        "use_auth_token": True if model_args.use_auth_token else None,
    }

    if model_args.tokenizer_name:

        if 'distill' in model_args.tokenizer_name:
            print("DISTILL tokenizer")
            ## load model and tokenizer
            tokenizer = GPT2Tokenizer.from_pretrained(model_args.tokenizer_name, **tokenizer_kwargs)
        else:
            tokenizer = AutoTokenizer.from_pretrained(model_args.tokenizer_name, **tokenizer_kwargs)

    elif model_args.model_name_or_path:
        tokenizer = AutoTokenizer.from_pretrained(model_args.model_name_or_path, **tokenizer_kwargs)
        


    else:
        raise ValueError(
            "You are instantiating a new tokenizer from scratch. This is not supported by this script."
            "You can do it from another script, save it, and load it from here, using --tokenizer_name."
        )

    #SPECIAL_TOKENS = ['[AMR]', '[SPARQL]']


    #tokenizer.add_tokens(SPECIAL_TOKENS)
    tokenizer.bos_token = '<s>'
    #tokenizer.eos_token = '</OUTPUT>'
    tokenizer.eos_token = '</s>'
    #tokenizer.pad_token = '[PAD]'
    #tokenizer.mask_token = '<MASK>'
    # tokenizer.sep_token = '<SEP>'


    if 'distil' in model_args.model_name_or_path:
        print("DISTILL MODEL")
        #model = GPT2LMHeadModel.from_pretrained(model_args.model_name_or_path)

        model = AutoModelForCausalLM.from_pretrained(
            model_args.model_name_or_path,
            from_tf=bool(".ckpt" in model_args.model_name_or_path),
            config=config,
            cache_dir=model_args.cache_dir,
            revision=model_args.model_revision,
            use_auth_token=True if model_args.use_auth_token else None,
        )

    elif 'phi' in model_args.model_name_or_path:

            model = AutoModelForCausalLM.from_pretrained(
                model_args.model_name_or_path,
                from_tf=bool(".ckpt" in model_args.model_name_or_path),
                config=config,
                cache_dir=model_args.cache_dir,
                revision=model_args.model_revision,
                use_auth_token=True if model_args.use_auth_token else None,
                ignore_mismatched_sizes=True
            )

    elif 'flan' in model_args.model_name_or_path:

        model =  AutoModelForSeq2SeqLM.from_pretrained(
            model_args.model_name_or_path,
            from_tf=bool(".ckpt" in model_args.model_name_or_path),
            config=config,
            cache_dir=model_args.cache_dir,
            revision=model_args.model_revision,
            use_auth_token=True if model_args.use_auth_token else None,
        )

    else:
        model = AutoModelForCausalLM.from_config(config)
        n_params = sum(dict((p.data_ptr(), p.numel()) for p in model.parameters()).values())
        logger.info(f"Training new model from scratch - Total size={n_params/2**20:.2f}M params")

    model.resize_token_embeddings(len(tokenizer))

    # Preprocessing the datasets.
    # First we tokenize all the texts.
    if training_args.do_train:
        column_names = raw_datasets["train"].column_names
    else:
        column_names = raw_datasets["validation"].column_names
    text_column_name = "text" if "text" in column_names else column_names[0]

    # since this will be pickled to avoid _LazyModule error in Hasher force logger loading before tokenize_function
    tok_logger = transformers.utils.logging.get_logger("transformers.tokenization_utils_base")

    def tokenize_function(examples):
        with CaptureLogger(tok_logger) as cl:
            output = tokenizer(examples[text_column_name])
        # clm input could be much much longer than block_size
        if "Token indices sequence length is longer than the" in cl.out:
            tok_logger.warning(
                "^^^^^^^^^^^^^^^^ Please ignore the warning above - this long input will be chunked into smaller bits before being passed to the model."
            )
        return output

    with training_args.main_process_first(desc="dataset map tokenization"):
        tokenized_datasets = raw_datasets.map(
            tokenize_function,
            batched=True,
            num_proc=data_args.preprocessing_num_workers,
            remove_columns=column_names,
            load_from_cache_file=not data_args.overwrite_cache,
            desc="Running tokenizer on dataset",
        )

    if data_args.block_size is None:
        block_size = tokenizer.model_max_length
        if block_size > 1024:
            logger.warning(
                f"The tokenizer picked seems to have a very large `model_max_length` ({tokenizer.model_max_length}). "
                "Picking 1024 instead. You can change that default value by passing --block_size xxx."
            )
            block_size = 1024
    else:
        if data_args.block_size > tokenizer.model_max_length:
            logger.warning(
                f"The block_size passed ({data_args.block_size}) is larger than the maximum length for the model"
                f"({tokenizer.model_max_length}). Using block_size={tokenizer.model_max_length}."
            )
        block_size = min(data_args.block_size, tokenizer.model_max_length)

    # Main data processing function that will concatenate all texts from our dataset and generate chunks of block_size.
    def group_texts(examples):
        # Concatenate all texts.
        concatenated_examples = {k: sum(examples[k], []) for k in examples.keys()}
        total_length = len(concatenated_examples[list(examples.keys())[0]])
        # We drop the small remainder, we could add padding if the model supported it instead of this drop, you can
        # customize this part to your needs.
        total_length = (total_length // block_size) * block_size
        # Split by chunks of max_len.
        result = {
            k: [t[i : i + block_size] for i in range(0, total_length, block_size)]
            for k, t in concatenated_examples.items()
        }
        result["labels"] = result["input_ids"].copy()
        return result

    # Note that with `batched=True`, this map processes 1,000 texts together, so group_texts throws away a remainder
    # for each of those groups of 1,000 texts. You can adjust that batch_size here but a higher value might be slower
    # to preprocess.
    #
    # To speed up this part, we use multiprocessing. See the documentation of the map method for more information:
    # https://huggingface.co/docs/datasets/package_reference/main_classes.html#datasets.Dataset.map

    with training_args.main_process_first(desc="grouping texts together"):
        lm_datasets = tokenized_datasets.map(
            group_texts,
            batched=True,
            batch_size=data_args.batch_size,
            num_proc=data_args.preprocessing_num_workers,
            load_from_cache_file=not data_args.overwrite_cache,
            desc=f"Grouping texts in chunks of {block_size}",
        )

    if training_args.do_train:
        if "train" not in tokenized_datasets:
            raise ValueError("--do_train requires a train dataset")
        train_dataset = lm_datasets["train"]
        if data_args.max_train_samples is not None:
            train_dataset = train_dataset.select(range(data_args.max_train_samples))

    if training_args.do_eval:
        if "validation" not in tokenized_datasets:
            raise ValueError("--do_eval requires a validation dataset")
        eval_dataset = lm_datasets["validation"]
        if data_args.max_eval_samples is not None:
            eval_dataset = eval_dataset.select(range(data_args.max_eval_samples))

        def preprocess_logits_for_metrics(logits, labels):
            if isinstance(logits, tuple):
                # Depending on the model and config, logits may contain extra tensors,
                # like past_key_values, but logits always come first
                logits = logits[0]
            return logits.argmax(dim=-1)

        metric = evaluate.load("accuracy")

        #metric = evaluate.load("sacrebleu")

        def compute_metrics(eval_preds):
            preds, labels = eval_preds
            # preds have the same shape as the labels, after the argmax(-1) has been calculated
            # by preprocess_logits_for_metrics but we need to shift the labels
            labels = labels[:, 1:].reshape(-1)
            preds = preds[:, :-1].reshape(-1)
            results = metric.compute(predictions=preds, references=labels)
            return results

    # Initialize our Trainer
    trainer = Trainer(
        model=model,
        args=training_args,
        train_dataset=train_dataset if training_args.do_train else None,
        eval_dataset=eval_dataset if training_args.do_eval else None,
        tokenizer=tokenizer,
        # Data collator will default to DataCollatorWithPadding, so we change it.
        data_collator=default_data_collator,
        compute_metrics=compute_metrics if training_args.do_eval and not is_torch_tpu_available() else None,
        preprocess_logits_for_metrics=preprocess_logits_for_metrics
        if training_args.do_eval and not is_torch_tpu_available()
        else None,
    )

    # Training
    if training_args.do_train:
        checkpoint = None
        if training_args.resume_from_checkpoint is not None:
            checkpoint = training_args.resume_from_checkpoint
        elif last_checkpoint is not None:
            checkpoint = last_checkpoint
        train_result = trainer.train(resume_from_checkpoint=checkpoint)
        trainer.save_model()  # Saves the tokenizer too for easy upload

        metrics = train_result.metrics

        max_train_samples = (
            data_args.max_train_samples if data_args.max_train_samples is not None else len(train_dataset)
        )
        metrics["train_samples"] = min(max_train_samples, len(train_dataset))

        trainer.log_metrics("train", metrics)
        trainer.save_metrics("train", metrics)
        trainer.save_state()

    # Evaluation

    MAX_LENGTH = data_args.max_gen_length

    results_to_save = []

    if training_args.do_eval:
    #if raw_datasets_gen:

        metrics = trainer.evaluate()

        bleu_two = datasets.load_metric('bleu')
        meteor = datasets.load_metric('meteor')
        rouge = datasets.load_metric('rouge')

        evaluation_data = ['validation_gen']

        for eval_d in evaluation_data:

            logger.info("*** Evaluate *** {} ***".format(eval_d))

            bleu_scores = []

            eval_sents = raw_datasets_gen[eval_d]['text']
            eval_labels_sparql = raw_datasets_gen[eval_d]['y_sparql']
            eval_labels_amr = raw_datasets_gen[eval_d]['y_amr']
            eval_labels_lang = raw_datasets_gen[eval_d]['language']
            eval_labels_corpus = raw_datasets_gen[eval_d]['corpus']

            for sent, lab_sparql, lab_amr, lab_lang, lab_corp in tqdm(zip(eval_sents, eval_labels_sparql, eval_labels_amr, eval_labels_lang, eval_labels_corpus)):
                #inputs = tokenizer.encode(sent, add_special_tokens=False, return_tensors="pt")

                #inputs = tokenizer.encode(sent, add_special_tokens=True, return_tensors="pt", padding=False)

                inputs = tokenizer(sent, add_special_tokens=False, return_tensors="pt", padding=False)
                encoded_prompt = {k: v.to("cuda") for k, v in inputs.items()}

                if data_args.search_type == 'greedy':

                    with torch.no_grad():

                        gen_output = model.generate(
                            **encoded_prompt, 
                            max_length=MAX_LENGTH,
                            no_repeat_ngram_size=4,
                            bos_token_id=tokenizer.bos_token_id,
                            eos_token_id=tokenizer.eos_token_id,
                            pad_token_id=tokenizer.pad_token_id
                        )

                elif data_args.search_type == 'beam':
                    with torch.no_grad():
                        gen_outputs = model.generate(
                            **encoded_prompt,
                            max_length=MAX_LENGTH,
                            temperature=data_args.temperature,
                            length_penalty=0.0,
                            num_beams=data_args.num_beams,
                            num_beam_groups=5,
                            num_return_sequences=5,
                            no_repeat_ngram_size=4,
                            top_p=data_args.p_sampling,
                            repetition_penalty=1.0,
                            diversity_penalty=1.0,
                            early_stopping=True,
                            return_dict_in_generate=True,
                            output_scores=True,
                            bos_token_id=tokenizer.bos_token_id,
                            eos_token_id=tokenizer.eos_token_id,
                            pad_token_id=tokenizer.pad_token_id                        
                        )

                else:

                    with torch.no_grad():

                        gen_output = model.generate(
                            **encoded_prompt,
                            max_length=MAX_LENGTH,
                            temperature=data_args.temperature,
                            no_repeat_ngram_size=4,
                            top_p=data_args.p_sampling,
                            repetition_penalty=1.0,
                            do_sample=True,
                            return_dict_in_generate=True,
                            output_scores=True,
                            bos_token_id=tokenizer.bos_token_id,
                            eos_token_id=tokenizer.eos_token_id,
                            pad_token_id=tokenizer.pad_token_id
                        )

                    
                if data_args.search_type == 'beam':

                    sys_output = []

                    print(f"Label sparql >{lab_sparql}")
                    print(f"Label amr >{lab_amr}")
                    print()
                    for g_output in gen_outputs.sequences:

                        ex_g_output = tokenizer.decode(g_output, skip_special_tokens=False)

                        # if tokenizer.eos_token in ex_g_output:
                        #     ex_g_output = ex_g_output.split(tokenizer.eos_token)[0]

                        #ex_g_output = ex_g_output.split('/n')[1:]

                        #sentence = ex_g_output.split('<s>')[1].strip()
                        #ex_g_output = re.search(pat, ex_g_output).group(0)
                        sys_output.append(ex_g_output)
                        # print(f"Sentence>{sentence}")
                        # print()
                        print(f"Language {lab_lang}")
                        print(f"Corpus {lab_corp}")
                        print(f"Sys_output beam>{ex_g_output}")
                        print()

                    #transition_scores_to_save = compute_transition_scores_func(generated_outputs, model, gen_outputs, tokenizer)

                    transition_scores_to_save = compute_beam_transition_scores_func_v2(inputs, gen_outputs, model, tokenizer)

                    test_instance = {"sentence": sent,
                                     "ref_sparql": lab_sparql,
                                     "ref_amr": lab_amr,
                                     "ref_language": lab_lang,
                                     "ref_corpus": lab_corp,
                                     "outputs": sys_output,
                                     "transition_scores": transition_scores_to_save}
                    results_to_save.append(test_instance)

                else:
                    
                    input_length = 1 if model.config.is_encoder_decoder else inputs.input_ids.shape[1]
                    generated_tokens = gen_output.sequences[:, input_length:]
                    generated_tokens_scores = gen_output.scores[input_length:]
                    sys_output = tokenizer.decode(generated_tokens[0], skip_special_tokens=True)

                    if tokenizer.eos_token in sys_output:
                        sys_output = sys_output.split(tokenizer.eos_token)[0]
                    print(f"Sys_output>{sys_output}")

                    transition_scores_to_save = compute_transition_scores_func(generated_tokens, generated_tokens_scores, model, gen_output, tokenizer)


            if data_args.do_metrics:

                bleu_mean = np.mean(bleu_scores)

                bleu_two_metric_dict = bleu_two.compute()
                meteor_metric_dict = meteor.compute()
                rouge_metric_dict = rouge.compute()

                metrics["bleu_{}".format(eval_d)] = "{:.3f}".format(bleu_mean)
                metrics["bleu_two_{}".format(eval_d)] = "{:.3f}".format(bleu_two_metric_dict["bleu"])
                metrics["meteor_{}".format(eval_d)] = "{:.3f}".format(meteor_metric_dict["meteor"])
                metrics["rougeL_{}".format(eval_d)] = "{:.3f}".format(rouge_metric_dict["rougeL"].mid.fmeasure)
                metrics["rouge2_{}".format(eval_d)] = "{:.3f}".format(rouge_metric_dict["rouge2"].mid.fmeasure)

        if data_args.do_metrics:
    
            max_eval_samples = data_args.max_eval_samples if data_args.max_eval_samples is not None else len(eval_dataset)
            metrics["eval_samples"] = min(max_eval_samples, len(eval_dataset))
            try:
                perplexity = math.exp(metrics["eval_loss"])
            except OverflowError:
                perplexity = float("inf")
            metrics["perplexity"] = perplexity

            trainer.log_metrics("eval", metrics)
            trainer.save_metrics("eval", metrics)

    if training_args.push_to_hub:
        kwargs = {"finetuned_from": model_args.model_name_or_path, "tasks": "text-generation"}
        if data_args.dataset_name is not None:
            kwargs["dataset_tags"] = data_args.dataset_name
            if data_args.dataset_config_name is not None:
                kwargs["dataset_args"] = data_args.dataset_config_name
                kwargs["dataset"] = f"{data_args.dataset_name} {data_args.dataset_config_name}"
            else:
                kwargs["dataset"] = data_args.dataset_name

        trainer.push_to_hub(**kwargs)


    if data_args.results_dir and len(results_to_save)>0:


        t = datetime.datetime.now()

        date = t.strftime('%Y-%m-%d-%H-%M')

        fname = data_args.results_dir+ f'results-{data_args.task}-{date}.json'

        print("Writing results to {}".format(fname))

        with open(fname, 'w') as outfile:
            json.dump(results_to_save, outfile, indent=4)

def _mp_fn(index):
    # For xla_spawn (TPUs)
    main()


if __name__ == "__main__":
    main()