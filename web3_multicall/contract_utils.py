# ------------------------------------------------------------ Imports ----------------------------------------------------------- #

# Pip
from web3._utils.abi import normalize_event_input_types, abi_to_signature
from web3.contract.contract import ContractFunction

# -------------------------------------------------------------------------------------------------------------------------------- #



# -------------------------------------------------------- Public functions ------------------------------------------------------ #

def method_signature(
    method: ContractFunction
) -> str:
    return "{fn_name}({fn_input_types})({fn_output_types})".format(
        fn_name=method.abi['name'],
        fn_input_types=','.join([
            arg['type'] for arg in normalize_event_input_types(method.abi.get('inputs', []))
        ]),
        fn_output_types=','.join([
            arg['type'] for arg in normalize_event_input_types(method.abi.get('outputs', []))
        ])
    )


# -------------------------------------------------------------------------------------------------------------------------------- #