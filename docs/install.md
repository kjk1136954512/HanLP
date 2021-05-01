# Install

```{figure} _static/install-versions.svg
---
width: 100%
figclass: caption
alt: HanLP versions
name: hanlp-versions
---
Choose your HanLP version
```

## Install RESTful Packages

[![Downloads](https://pepy.tech/badge/hanlp-restful)](https://pepy.tech/project/hanlp-restful) [![Downloads](https://pepy.tech/badge/hanlp-restful/month)](https://pepy.tech/project/hanlp-restful) [![Downloads](https://pepy.tech/badge/hanlp-restful/week)](https://pepy.tech/project/hanlp-restful) 

```{eval-rst}
.. margin:: **Beginners Attention**

    .. Hint:: New to NLP? Just install RESTful packages and call :meth:`~hanlp_restful.HanLPClient.parse` without pain.
```

For beginners, the recommended RESTful packages are easier to start with. 
The only requirement is [an auth key](https://bbs.hankcs.com/t/apply-for-free-hanlp-restful-apis/3178). 
We officially released the following language bindings:

### Python

```shell script
pip install hanlp_restful
```

### Java

See [Java instructions](https://hanlp.hankcs.com/docs/api/restful_java.html).

### Golang

See [Golang instructions](https://hanlp.hankcs.com/docs/api/restful_golang.html).

## Install Native Package

[![Downloads](https://pepy.tech/badge/hanlp)](https://pepy.tech/project/hanlp) [![Downloads](https://pepy.tech/badge/hanlp/month)](https://pepy.tech/project/hanlp) [![Downloads](https://pepy.tech/badge/hanlp/week)](https://pepy.tech/project/hanlp)  

The native package running locally can be installed via pip.

```
pip install hanlp
```

HanLP requires Python 3.6 or later. GPU/TPU is suggested but not mandatory. Depending on your preference, HanLP offers the following flavors:

````{margin} **Windows Support**
```{note}
Installation on Windows is **perfectly** supported. The full version `hanlp[full]` additionally requires 
[Microsoft Visual C++ Build Tools](http://go.microsoft.com/fwlink/?LinkId=691126) to compile C++ extensions. 
```
````

| Flavor  | Description                                                  |
| ------- | ------------------------------------------------------------ |
| default | This installs the default version which delivers the most commonly used functionalities. However, some heavy dependencies like TensorFlow are not installed. |
| full    | For experts who seek to maximize the efficiency via TensorFlow and C++ extensions, `pip install hanlp[full]` installs every dependency HanLP will use in production. |

## Install Models

In short, you don't need to manually install any model. Instead, they are automatically downloaded to a directory called `HANLP_HOME` when you call `hanlp.load`.
Occasionally, some errors might occur the first time you load a model, in which case you can refer to the following tips.

### Download Error

If the auto-download fails, you can either:

1. Retry as our file server might be busy serving users from all over the world.
2. Follow the message on your terminal, which often guides you to manually download a `zip` file to a particular path. 
3. Use a [mirror site](https://hanlp.hankcs.com/docs/configure.html#use-mirror-sites) which could be faster and stabler in your region.
4. If the log shows errors of Hugging Face 🤗 Transformers, try ``export HF_MIRROR=tuna`` to use the [tuna mirror site](https://mirrors.tuna.tsinghua.edu.cn/help/hugging-face-models/).

### Server without Internet

If your server has no Internet access at all, just debug your codes on your local PC and copy the following directories to your server via a USB disk.

1. `~/.hanlp`: the home directories for HanLP models.
2. `~/.cache/huggingface`: the home directory for Hugging Face 🤗 Transformers. 
    - If the locale of your PC is ``zh_CN`` then the transformer models are downloaded from the [tuna mirror site](https://mirrors.tuna.tsinghua.edu.cn/help/hugging-face-models/). Make sure your server is also using ``zh_CN`` otherwise you may want to ``export HF_MIRROR=tuna`` on your server.

### Import Error

Some TensorFlow/fastText models will ask you to install the missing TensorFlow/fastText modules, in which case you'll need to install the full version:

```shell script
pip install hanlp[full]
```


```{caution}
DO NOT install TensorFlow/fastText by yourself, as higher or lower versions of TensorFlow have not been tested and might not work properly. 
```