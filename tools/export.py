import os
import torch
from nanodet.model.arch import build_model
from nanodet.util import Logger, cfg, load_config, load_model_weight


def main(config, model_path, output_path, input_shape=(320, 320)):
    logger = Logger(-1, config.save_dir, False)
    model = build_model(config.model)
    checkpoint = torch.load(model_path, map_location=lambda storage, loc: storage)
    load_model_weight(model, checkpoint, logger)
    dummy_input = torch.autograd.Variable(torch.randn(1, 3, input_shape[0], input_shape[1]))
    torch.onnx.export(model, dummy_input, output_path, verbose=True, keep_initializers_as_inputs=True, opset_version=11)
    print('finished exporting onnx ')


def onnx_simplifier(in_model, simplified_model_path):
    """
    simplify ONNX model
    :param in_model_path: original ONNX model path
    :param simplified_model_path
    :return:
    """
    try:
        import onnx
    except ImportError:
        exit("Please install onnx using command: pip install onnx")
    try:
        from onnxsim import simplify
    except ImportError:
        exit("Please install onnx simplifier using command: pip install onnx-simplifier")

    model = onnx.load(in_model)
    s_model, check = simplify(model)
    assert check, "Simplified ONNX model could not be validated"
    onnx.save(s_model, simplified_model_path)


if __name__ == '__main__':
    cfg_path = r"../config/nanodet-m.yml"  # config file with extension .yml
    model_path = r"workspace/nanodet_m/model_last.pth"  # trained model path with extension .pth
    out_path = r'output.onnx'  # the path for output file in onnx framework
    simplify_mode = False
    load_config(cfg, cfg_path)
    main(cfg, model_path, out_path, input_shape=(320, 320))
    if simplify_mode:
        onnx_simplifier(out_path, 'simplify_output.onnx')
