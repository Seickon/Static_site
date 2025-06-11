from enum import Enum

"""
def markdown_to_blocks(markdown):
    #blocks = markdown.strip()
    blocks = blocks.split("\n\n")
    i = 0
    for block in blocks:
        block = block.strip()
        if block == "":
            del blocks[i]
            i -= 1
        i += 1
    return blocks

def block_to_block_type(block=""):
        lines = block.splitlines()
        match block[0]:
            case "#":
                n = 1
                while True:                    
                    if block[n] == "#":
                        n += 1
                        continue
                    elif block[n] == " " and n < 7:
                        return BlockType.HEADING
                    break
            
            case "`":
                if block[0:3] == "```" and block[-3:] == "```":
                    return BlockType.CODE
            
            case ">":
                check = 0
                for line in lines:
                    if line[0] == ">":
                        check += 1
                if check == len(lines):
                    return BlockType.QUOTE
            
            case "-":
                check = 0
                for line in lines:
                    if line[:2] == "- ":
                        check += 1
                if check == len(lines):
                    return BlockType.UNORDERED_LIST
            
            case "1":
                check = 0
                count = 1                
                for line in lines:
                    slicer = len(str(count)) + 2
                    if line[:slicer] == f"{count}. ":
                        check += 1
                        count += 1
                if check == len(lines):
                    return BlockType.ORDERED_LIST
                True
                
        return BlockType.PARAGRAPH
"""

class BlockType(Enum):
    PARAGRAPH = "normal"
    HEADING = "heading"
    CODE = "code"
    QUOTE = "quote"
    UNORDERED_LIST = "unordred List"
    ORDERED_LIST = "ordered list"


def markdown_to_blocks(markdown):
    blocks = markdown.split("\n\n")
    filtered_blocks = []
    for block in blocks:
        if block == "":
            continue
        block = block.strip()
        filtered_blocks.append(block)
    return filtered_blocks

def block_to_block_type(block):
    lines = block.split("\n")

    if block.startswith(("# ", "## ", "### ", "#### ", "##### ", "###### ")):
        return BlockType.HEADING
    if len(lines) > 1 and lines[0].startswith("```") and lines[-1].startswith("```"):
        return BlockType.CODE
    if block.startswith(">"):
        for line in lines:
            if not line.startswith(">"):
                return BlockType.PARAGRAPH
        return BlockType.QUOTE
    if block.startswith("- "):
        for line in lines:
            if not line.startswith("- "):
                return BlockType.PARAGRAPH
        return BlockType.UNORDERED_LIST
    if block.startswith("1. "):
        i = 1
        for line in lines:
            if not line.startswith(f"{i}. "):
                return BlockType.PARAGRAPH
            i += 1
        return BlockType.ORDERED_LIST
    return BlockType.PARAGRAPH