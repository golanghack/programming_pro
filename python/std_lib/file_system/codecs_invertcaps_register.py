#! /usr/bin/env python3 

import codecs
from codecs_invertcaps_charmap import encoding_map, decoding_map

class InvertCapsCodec(codecs.Codec):
    """Encode/Decode without save set."""
    
    def encode(self, input_: str, errors: str='strict'):
        return codecs.charmap_encode(input_, errors, encoding_map)
    
    def decode(self, input_: str, errors: str='strict'):
        return codecs.charmap_decode(input_, errors, decoding_map)
    
class InvertCapsIncrementalEncoder(codecs.IncrementalEncoder):
    
    def encode(self, input_: str, final: bool=False):
        data, htypes = codecs.charmap_encode(input_, self.errors, encoding_map)
        return data 
    
class InvertCapsIncrementalDecoder(codecs.IncrementalDecoder):
    
    def decode(self, input_: str, final: bool=False):
        data, hbytes = codecs.charmap_decode(input_, self.errors, decoding_map)
        return data
    

class InvertCapsStreamReader(InvertCapsCodec, codecs.StreamReader):
    pass

class InvertCapsStreamWriter(InvertCapsCodec, codecs.StreamWriter):
    pass

def find_invertcaps(encoding):
    """ 
    Return codec for 'invertcaps'
    """
    
    if encoding == 'invertcaps':
        return codecs.CodecInfo(
            name='invertcaps', 
            encode=InvertCapsCodec().encode, 
            decode=InvertCapsCodec().decode, 
            incrementalencoder=InvertCapsIncrementalEncoder, 
            incrementaldecoder=InvertCapsIncrementalDecoder, 
            streamreader=InvertCapsStreamReader, 
            streamwriter=InvertCapsStreamWriter,
        )
    return None
    
codecs.register(find_invertcaps)

if __name__ == '__main__':
    # encoder/decoder without save set
    encoder = codecs.getencoder('invertcaps')
    text = 'AAAaaaAAA'
    encoded_text, consumed = encoder(text)
    print(f'Encoded "{text}" to "{encoded_text}", consuming {consumed} characters')
    
    # object record thread
    import io 
    
    buffer = io.BytesIO()
    writer = codecs.getwriter('invertcaps')(buffer)
    print('StreamWriter for io buffer -> ')
    print('writing "AAAaaaAAA')
    writer.write('AAAaaaAAA')
    print(' buffer contents -> ', buffer.getvalue())
    
    # incremental decode
    decoder_factory = codecs.getincrementaldecoder('invertcaps')
    decoder = decoder_factory()
    decoded_text_parts = []
    for c in encoded_text:
        decoded_text_parts.append(decoder.decode(bytes([c]), final=False))
    decoded_text_parts.append(decoder.decode(b'', final=True))
    decoded_text = ''.join(decoded_text_parts)
    print(f'IncrementalDecoder converted -> {encoded_text!r} to -> {decoded_text!r}')

        