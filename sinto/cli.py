from sinto import (
    utils,
    filterbarcodes,
    addtags,
    fragments,
    tagtorg,
    addbarcodes,
    tagtotag,
    tagtoname,
    blocks
)


@utils.log_info
def run_filterbarcodes(options):
    """Wraps the sinto.filterbarcodes function for use on the command line
    """
    filterbarcodes.filterbarcodes(
        cells=options.cells,
        bam=options.bam,
        trim_suffix=options.trim_suffix,
        nproc=options.nproc,
        readname_barcode=options.barcode_regex,
        cellbarcode=options.barcodetag,
        outdir=options.outdir,
        sam=options.sam
    )


@utils.log_info
def run_addtags(options):
    """Wraps the sinto.addtags function for use on the command line
    """
    addtags.addtags(
        bam=options.bam,
        tagfile=options.tagfile,
        trim_suffix=options.trim_suffix,
        output=options.output,
        sam=options.sam,
        nproc=options.nproc,
        mode=options.mode,
    )


@utils.log_info
def run_fragments(options):
    """Wraps the sinto.fragments function for use on the command line
    """
    fragments.fragments(
        bam=options.bam,
        fragment_path=options.fragments,
        min_mapq=options.min_mapq,
        nproc=options.nproc,
        cellbarcode=options.barcodetag,
        readname_barcode=options.barcode_regex,
        chromosomes=options.use_chrom,
        cells=options.cells,
        max_distance=options.max_distance,
        min_distance=options.min_distance,
        chunksize=options.chunksize,
        shifts=[options.shift_plus, options.shift_minus],
        collapse_within=options.collapse_within,
        temp_dir=options.temp_dir
    )


@utils.log_info
def run_tagtorg(options):
    tagtorg.tagtorg(
        bam=options.bam,
        tag_value_file=options.tagfile,
        tag=options.tag,
        output=options.output,
        out_format=options.outputformat,
    )


@utils.log_info
def run_blocks(options):
    blocks.blocks(
        bam=options.bam,
        block_path=options.blocks,
        min_mapq=options.min_mapq,
        nproc=options.nproc,
        cellbarcode=options.barcodetag,
        umibarcode=options.umitag,
        readname_barcode=options.barcode_regex,
        cells=options.cells,
        include_strand=options.strand,
    )

@utils.log_info
def run_tagtotag(options):
    tagtotag.tagtotag(
        bam=options.bam,
        from_tag=options.from_,
        to_tag=options.to,
        output=options.output,
        delete=options.delete,
        out_format=options.outputformat,
    )


@utils.log_info
def run_barcode(options):
    addbarcodes.addbarcodes(
        cb_position=options.bases,
        fq1=options.barcode_fastq,
        fq2=options.read1,
        fq3=options.read2,
        prefix=options.prefix,
        suffix=options.suffix,
    )

@utils.log_info
def run_tagtoname(options):
    tagtoname.move(
        bam=options.bam,
        output=options.output,
        cb_tag=options.tag,
        out_format=options.outputformat,
        from_tag=True
    )

@utils.log_info
def run_nametotag(options):
    tagtoname.move(
        bam=options.bam,
        output=options.output,
        cb_tag=options.tag,
        out_format=options.outputformat,
        from_tag=False,
        cb_regex=options.barcode_regex
    )
